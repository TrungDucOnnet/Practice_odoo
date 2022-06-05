from odoo import fields, models, api, tools, _
from odoo.exceptions import UserError, ValidationError

class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="School Name", help="This is school name", required=True, default="This is default shool name", size=15, copy=False)
    email = fields.Char(string="School Email")
    phone = fields.Char(string="School Phone", groups="school_weblearn.access_school_mid_level_group")
    is_vitural_class = fields.Boolean(string="Vitural Class Support?", default=True)
    school_rank = fields.Integer(string="Rank", default=lambda lm: lm.get_default_rank())
    result = fields.Float(string="Result", readonly=True, default=1.155, digits=(3, 4))
    address = fields.Text(string="Address", default="This is deault address")
    establish_date= fields.Date(string="Establish Day", default=fields.Date.today())
    open_date= fields.Datetime(string="Open Day", default=fields.Datetime.now())
    school_type = fields.Selection([('public', 'Public School'), ('private', 'Private School')], string='School Type')
    documents = fields.Binary(string="Document")
    file_name = fields.Char(string="File Name")
    school_image = fields.Image(string="School Image", max_width=100, max_height=100)
    school_description = fields.Html(string="School Description")
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto Rank", store=True)
    school_seq_name = fields.Char("School Code")
    test = fields.Char("Test context default")

    @api.depends('school_type')
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "public":
                rec.auto_rank = 50
            elif rec.school_type == "private":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0
    def get_default_rank(self):
        if 1 == 1:
            return 100
        else:
            return 200

    @api.model
    def create(self, vals):
        vals['school_seq_name'] = self.env['ir.sequence'].next_by_code("school.profile")

        is_check_duplicated_name = self.env['ir.config_parameter'].sudo().get_param('schoolprofile.is_check_duplicated_name', default=False)
        if is_check_duplicated_name:
            vals = [vals,] if not isinstance(vals, (tuple, list)) else vals
            for val in vals:
                school_name = val["name"]
                school_records = self.search([('name', '=', school_name)])
                if school_records:
                    raise ValidationError(_("Duplicated school name @ %s" % school_name))
        # new_context = self.env.context
        # new_context['default_test']='abc'
        rtn = super(SchoolProfile, self.with_context(default_test='abc')).create(vals)
        return rtn

    def custom_remove(self):
        for school in self:
            school.unlink()

    def name_get(self):
        list = []
        for school in self:
            name = school.name
            if school.school_type:
                name += "({})".format(school.school_type)
            list.append((school.id, name))
        return list

    # Tao moi record trong One2Many field
    def specialCommand(self):
        # First way to create child model for exitsting parent model
        # student_obj = self.env['student.profile']
        # stu_id = student_obj.create({'name':"Student One", 'school_id': self.id})

        #Using Special Commnand
        # self.create({'name': 'Aptech', 'school_list': [(0, 0, {'name': 'Student Aptech 1'}),
        #                                                (0, 0, {'name': 'Student Aptech 2'}),
        #                                                (0, 0, {'name': 'Student Aptech 3'}),
        #                                                (0, 0, {'name': 'Student Aptech 4'}),
        #                                                (0, 0, {'name': 'Student Aptech 5'}),
        #                                                ]})

        # self.write({'school_list': [(0, 0, {'name': 'Student Aptech 6'})]})
        pass

    # Update record trong One2Many field
    def specialCommand1(self):
        # for student in self.school_list:
        #     student.name = student.name + " - " + str(student.id)
        #     student.student_fees = 1000
        #     student.total_fees = 5000

        #We can use to update operation for parent and child model
        # vals = {'school_list': []}
        # for student in self.school_list:
        #     vals['school_list'].append([1, student.id, {'name': student.name + "Name"}])
        #
        # self.write(vals)

        #No need to use like this (
        # for student in self.school_list:
        #     student.update({'name': student.name + "Update by method update", 'total_fees': 2000})

        #Can be used instead of Speical commands
        for student in self.school_list:
            student.write({'name': student.name + "Update by write update", 'total_fees': 3000})

    #Xoa record trong One2Many field
    def specialCommand2(self):
        self.write({'school_list': [(2, 47, 0), (2, 48, 0)]})

    # Unlink record trong One2Many field
    def specialCommand3(self):
        self.write({'school_list': [(3, 50, 0), (3, 51, 0)]})

    def specialCommand4(self):
        self.write({'school_list': [(4, 50, 0), (4, 51, 0)]})

    def specialCommand5(self):
        # self.write({'school_list': [(5, 0, 0)]})
        self.school_list = [(5, 0, 0)]



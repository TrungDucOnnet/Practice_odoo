from odoo import fields, models, api, _
from odoo.exceptions import UserError

class Partner(models.Model):
    _inherit = "res.partner"


    def hello_hook(self):
        for contact in self.search([]):
            print(contact.display_name)

class Address(models.Model):
    _name="address"
    _rec_name="street"

    street = fields.Char(string="Street")
    street_one = fields.Char(string="Street 2")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")
    zip_code = fields.Char(string="Zip Code")


class StudentProfile(models.Model):
    _name = "student.profile"
    _inherit = ["mail.thread", 'mail.activity.mixin', "address"]
    _order = "name asc, id desc"
    _sql_constraints = [('name_unique', 'UNIQUE(name)', 'Please enter another name this name is exits'),
                        # ('fees_check', 'check (student_fees > 0)', 'Please check Student fees must be greater than 0'),
                        # ('total_fees_check', 'check (total_fees > 0.0)', 'Please check total fees must be greater than 0')
                        ]

    name = fields.Char(string=" Name", required=True, tracking=True)
    student_seq= fields.Integer(string="Student Sequence")
    roll_number = fields.Char(string="Roll Number")
    school_id = fields.Many2one('school.profile', string='School')
    hobby_list = fields.Many2many('hobby', 'school_hobby_el', 'student_id', 'hobby_id', string = "Hobbies")
    is_vitural_school = fields.Boolean(related="school_id.is_vitural_class", string="Is Vitural Class", store=True)
    ref_id = fields.Reference(selection=[('school.profile', 'School'),
                               ('account.move', 'Invoice')],
                              string="Reference Field",
                              default="school.profile,3")
    currency_id = currency_id = fields.Many2one('res.currency', string="Currency")
    student_fees = fields.Monetary(string="Student Fee", default=1900.25)
    total_fees = fields.Float(string="Total Fees")
    bdate = fields.Datetime(string="Due Date For Fees")
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection([('draft', 'Draft'), ('progress', 'Progress'), ('paid', 'Paid'), ('done', 'Done')], string="State")
    student_img = fields.Image(string = "Student Image")
    time_open_school = fields.Datetime(string="Open School Day", related="school_id.open_date")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    teacher_id = fields.Many2one('res.users', string='Teacher')
    hide_price_hobby = fields.Boolean(string="Hide Price Hobby")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Mức độ ưu tiên")
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color 2")
    total_fees_test=fields.Float(string="Total Fees Test", compute="_total_fees_test")


    @api.depends('total_fees')
    def _total_fees_test(self):
        self.total_fees_test = False
        if self.total_fees:
            self.total_fees_test = self.total_fees + 1000

    def specialCommand6(self):
        self.write({'hobby_list': [(6, 0, [3,4])]})

    def redirect_url(self):
        return {
            'type': "ir.actions.act_url",
            'url': "https://www.google.com/"
        }

    @api.model
    def _change_roll_number(self, add_string):
        """This method is used to add roll number to the student profile"""
        for stud in self.search([('roll_number', '=', False)]):
            stud.roll_number = add_string + "STD" + str(stud.id)

    def wiz_open(self):
        # return self.env['ir.actions.act_window']._for_xml_id('student_weblearn.student_fees_update_action')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'student.fees.update.wizard',
            # Loai view nao se duoc hien thi
            'view_mode': 'form',
            'target': 'new'
        }

    def write(self, vals):
        vals['active']=True
        rtn = super(StudentProfile, self).write(vals)
        return rtn

    @api.returns('self', lambda value: value.id)
    def copy(self, default={}):
        default['name'] = "copy ("+self.name+")"
        rtn = super(StudentProfile, self).copy(default=default)
        return rtn

    def unlink(self):
        rtn = super(StudentProfile, self).unlink()
        return rtn

    @api.model
    def name_create(self, name):
        rtn = self.create({'name': name, 'is_vitural_school': True})
        return rtn.name_get()[0]

    @api.model
    def default_get(self, field_lists):
        rtn = super(StudentProfile, self).default_get(['active', 'student_fees', 'total_fees'])
        rtn['name']='This is default student name'
        return rtn


class SchoolProfile(models.Model):
    _inherit = "school.profile"
    school_list = fields.One2many('student.profile', 'school_id', string="School List")

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('email', operator, name), ('school_type', operator, name)]
        school_ids = self._search(domain+args, limit=limit)
        return school_ids



    # @api.model
    # def create(self, vals):
    #     rtn = super(SchoolProfile, self).create(vals)
    #     if not rtn.school_list:
    #         raise UserError(_("Student List is empty"))
    #     return rtn




class Hobby(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")
    price = fields.Float("Price")

class Subject(models.Model):
    _name = "subject"

    name = fields.Char("Name")
    mark = fields.Float("Mark")

class Partner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        print("User Enviroment", self.env)
        print("User Enviroment", self.env.user)
        print("User Enviroment", self.env.company)
        print("User Enviroment", self.env.companies)
        print("User Enviroment", self.env.context)
        print("Partner value", vals)
        return self.super(Partner, self).create(vals)

class Car(models.Model):
    _name = "car"

    name = fields.Char("Car Name")
    price = fields.Char("Cost")

class CarEngine(models.Model):
    _name="car.engine"
    _inherits = {"car":"car_id"}

    name = fields.Char("Car Engine Name")
    car_id = fields.Many2one("car", string="Car")

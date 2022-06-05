from odoo import api, fields, models

class SchoolInformation(models.Model):
    _name = 'school.information'
    _inherit = 'mail.thread'
    _description = 'School Management'

    name = fields.Char(string='SchoolName', translate=True)
    type = fields.Selection([('Private', 'Dan lap') , ('Public', 'Cong lap')], default = 'Public', string='SchoolType')
    email = fields.Char(string='Email', translate=True)
    address = fields.Char(string='Address', required=True, translate=True)

    phone = fields.Char(string='School Phone Number')
    hasOnlineClass = fields.Boolean(string='Is There Any Online Class')
    rank = fields.Integer(string='Ranking Number')
    establishDay = fields.Date(string='School Establish Day')
    document = fields.Binary(string='School Document')
    document_name = fields.Char(string='Document Name')
    biography = fields.Html()
    classList = fields.One2many(comodel_name='class.information', inverse_name='school_id', string='Class List')
    tuition = fields.Float(compute="_auto_count_tuition", string="Hoc Phi 1 ky")


    @api.depends("type")
    def _auto_count_tuition(self):
        for re in self:
            if re.type == "Private":
                re.tuition = 10000000
            else:
                re.tuition = 5000000

    @api.onchange("name")
    def _onchange_name(self):
        if self.name == "":
            return {
                'warning': {
                    'title': "Warning",
                    'message': "You have to fill Name Value"
                }
            }

    @api.model
    def create(self, vals_list):
        res = super(SchoolInformation, self).create(vals_list)
        return res

    def write(self, vals):
        # a = self.env['class.information'].search([])
        res = super(SchoolInformation, self).write(vals)
        self.search([])
        return res

    #Creat value to any fields when create new record
    def default_get(self, fields_list):
        res = super(SchoolInformation, self).default_get(fields_list)
        res['address'] = 'Default Address'
        return res

    def name_create(self, name):
        res = super(SchoolInformation, self).name_create(name)

    def button_update_schoolname(self):
        self.write({"name": "Default Name"})

    def button_copy_school(self):
        self.copy({"name": "Copy Name"})

    def creat_record(self):
        self.name_create("Dai Hoc")

    def creat_record_hanoi(self):
        self.create([{'name':'Truong DH o HN','address': 'HaNoi'}])
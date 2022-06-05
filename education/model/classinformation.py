from odoo import api, fields, models

class ClassInformation(models.Model):
    _name = 'class.information'
    _description = 'Class Management'

    name=fields.Char(string="Class Name")
    grade=fields.Char(string="Grade")
    mainTeacher = fields.Char(string="Main Teacher")
    school_id = fields.Many2one("school.information", string="School", required=True)

    address = fields.Char(related='school_id.address', string="Dia chi Truong")

    @api.model
    def create(self, vals_list):
        res = super(ClassInformation, self).create(vals_list)
        self.env['school.information'].create([{'name': 'Newschool'}])
        return res
from odoo import fields, models, api, _
from odoo.exceptions import UserError

class CreateStudentWiz(models.TransientModel):
    _name = "create.student.wizard"
    _description="Create Student Wizard"

    name = fields.Char(string="Name", required=True)
    school_id = fields.Many2one('school.profile', string='School')

    def action_create_student(self):
        vals = {
            'name': self.name,
            'school_id' : self.school_id
        }
        result = self.env['student.profile'].create(vals)
        return result



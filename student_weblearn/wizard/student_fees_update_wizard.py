from odoo import models, fields

class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.fees.update.wizard"

    total_fees = fields.Float(string="Fees")

    def update_student_fees(self):
        self.env['student.profile'].browse(self.env.context['active_ids']).write({'total_fees': self.total_fees})
        return True

class StudentFeesUpdateExtendWizard(models.TransientModel):
    _inherit = "student.fees.update.wizard"

    parent_name = fields.Char(string="Parent Name")

    def update_student_fees(self):
        print("This is inherit method of update_student_fees(self) method")

        # return True
        # Without statement super

        #Use statement super
        variable = super(StudentFeesUpdateExtendWizard, self).update_student_fees()
        return variable
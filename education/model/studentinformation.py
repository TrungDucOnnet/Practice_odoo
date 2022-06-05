from odoo import api, fields, models

class StudentInformation(models.Model):
    _name = 'student.information'
    _description = 'Student Management'

    name=fields.Char(string="Student Name")
    birthday=fields.Date(string="Student Birthday")
    class_id = fields.Many2one("class.information", string="Student Class", required=True)
    school_id = fields.Many2one(related="class_id.school_id", string="School")
    subjectList = fields.Many2many("subject.information", "student_subject_relationship", "student_id", "subject_id", string = "Bang Quan He Mon Hoc Va Hoc Sinh")
    fee_per_semester = fields.Float(related="school_id.tuition")
    number_semester = fields.Integer(compute="_calculate_number_semester", string="Number Of Semester")
    grade = fields.Char(relate="class_id.grade", string="Grade")
    currency_id = fields.Many2one('res.currency', string="Money Unit")
    tuition = fields.Monetary(compute="_calculate_all_money", string="Tong Hoc Phi")
    color = fields.Integer(string='Color')

    @api.depends('grade')
    def _calculate_number_semester(self):
        for rec in self:
            if rec.grade == "10":
                rec.number_semester = 2
            elif rec.grade == "11":
                rec.number_semester = 4
            else:
                rec.number_semester = 6

    @api.depends('number_semester', 'fee_per_semester')
    def _calculate_all_money(self):
        for rec in self:
           rec.tuition = rec.number_semester * rec.fee_per_semester

class ClassInformation(models.Model):
    _inherit = 'class.information'
    studentList = fields.One2many("student.information", "class_id", string="Danhsachhocsinh")

class SubjectInformation(models.Model):
    _name = 'subject.information'
    _description = 'Subject Management'

    name = fields.Char(string="Subject Name")
    numberOfCer = fields.Integer(string = "Number Of Certificate")
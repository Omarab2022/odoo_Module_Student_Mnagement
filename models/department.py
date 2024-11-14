from odoo import models, fields, api

class Department(models.Model):
    _name = 'studentmanagement.department'
    _description = 'Department Management'

    name = fields.Char("Department name", required=True)
    code = fields.Char("Code", required=True)
    chief_id = fields.Many2one('res.users', string="Department Chief", required=True)
    student_ids = fields.Many2many(
        'studentmanagement.student',
        'department_student_rel',
        'department_id',
        'student_id',
        string="Students"
    )
    total_students = fields.Integer(
        string="Total Students",
        compute='_compute_total_students',
        store=True
    )

    @api.depends('student_ids')
    def _compute_total_students(self):
        for record in self:
            record.total_students = len(record.student_ids)
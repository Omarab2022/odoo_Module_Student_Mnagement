from odoo import api, models, fields

class Student(models.Model):
    _name = 'studentmanagement.student'
    _description = 'Student Management'

    fileNumber = fields.Char(
        string="File Number",
        required=True,
        readonly=True,  # Make it readonly
        default=lambda self: self.env['ir.sequence'].next_by_code('student.student.sequence') or '/'
    )
    lastName = fields.Char(string="Last Name", required=True)
    firstName = fields.Char(string="First Name", required=True)
    dateOfBirth = fields.Date(string="Date Of Birth")
    email = fields.Char(string="Email", required=True)
    phoneNumber = fields.Integer(string="Phone Number", required=True)
    cin = fields.Char(string="CIN", required=True)
    cne = fields.Char(string="CNE", required=True)
    paid = fields.Selection([('paid', 'Yes'), ('notPaid', 'No')], string="Paid", required=True)
    department_ids = fields.Many2many(
        'studentmanagement.department',
        'department_student_rel',
        'student_id',
        'department_id',
        string="Departments",
        required=True,
        ondelete='restrict'
    )

    @api.model
    def create(self, vals):
        if vals.get('fileNumber', '/') == '/':
            vals['fileNumber'] = self.env['ir.sequence'].next_by_code('student.student.sequence') or '/'
        return super(Student, self).create(vals)
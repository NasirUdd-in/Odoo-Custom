from odoo import api, fields, models, _


class TeacherTeacher(models.Model):
    _name = "teacher.teacher"
    _order = "name"
    _description = "Teacher"

    empid= fields.Integer(string="Employee Id", required= True)  
    name = fields.Char(string="Name", compute="_compute_name", store=True)
    firstname = fields.Char(string="Firstname", required=True)
    lastname = fields.Char(string="Lastname", required=True)

    deperment = fields.Char(string="Deperment", required=True)
    district = fields.Char(string="District", required=True)
    age = fields.Integer(string="Age", required= True)
    gender = fields.Selection ([ 
        ('male', 'Male'),
        ('female', 'Female'),

    ])
        
    @api.depends('firstname','lastname')

    def _compute_name(self):
        if self.firstname and self.lastname:
            self.name=self.firstname + ' ' + self.lastname

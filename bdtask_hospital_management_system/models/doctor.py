from odoo import api, fields, models, _


class DoctorDoctor(models.Model):
    _name = "doctor.doctor"
    _order = "name"
    _description = "Doctor"

    name = fields.Char(string="Name", required=True)
    department = fields.Char(string="Department", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection ([ 
        ('male', 'Male'),
        ('female', 'Female'),

    ])
 


        


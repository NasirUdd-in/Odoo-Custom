from odoo import api, fields, models, _

class PatientPatient(models.Model):
    _name = "patient.patient"
    _order = "name"
    _description = "Patient"

    name = fields.Char(string="Name")
    department = fields.Char(string="Department")
    age = fields.Integer(string="Age")
    gender = fields.Selection ([ 
        ('male', 'Male'),
        ('female', 'Female'),

    ])
from odoo import api, fields, models
from datetime import date

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string= 'Name')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    ref= fields.Char(string= "reference")
    gender = fields.Selection([('male','Male'), ('female', 'Female')], string="Gender")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")
    
    @api.depends('date_of_birth')
    def _compute_age(self):  
        for rec in self:
            today = date.today()
            print(date.today())
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
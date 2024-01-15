from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Patient"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    doctor_name = fields.Char(string='Doctor Name')
    date = fields.Date(string="Date")
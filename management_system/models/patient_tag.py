from odoo import api, fields, models

class PatientTagmodels(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
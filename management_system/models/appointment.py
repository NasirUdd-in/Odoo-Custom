from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Patient"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    doctor_name = fields.Char(string='Doctor Name')
    date = fields.Date(string="Date")
    ref= fields.Char(string= "reference")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority", help='Gives the sequence order when displaying a list of MRP documents.')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Cousultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled')], default='draft', string="Status", required=True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines','appointment_id', string='Pharmacy Lines')
    
    @api.onchange('patient_id')
    def onChange_patient_id(self):
        self.ref = self.patient_id.ref
    
    def action_in_consultaion(self):
        for rec in self:
            rec.state = 'in_consultation'
            
            
    def action_done(self):
        for rec in self:
            rec.state = 'done'
            
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
            
            

class AppointmentPharmacy(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"
    
    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
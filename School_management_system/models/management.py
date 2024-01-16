from odoo import api, fields, models, _


class ManagementManagement(models.Model):
    _name = "management.management"
    _order = "studentname"
    _description = "Management"

      
    studentname = fields.Char(string="Student Name", required=True)
    studentFee = fields.Integer(string="Student Fee", required= True)
    teachername = fields.Char(string="Teacher Name", required=True)
    teacherSalary = fields.Integer(string="Teacher Salary", required= True)
    

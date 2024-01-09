# my_module/models/task.py

from odoo import models, fields

class Task(models.Model):
    _name = 'my_module.task'
    _description = 'Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')

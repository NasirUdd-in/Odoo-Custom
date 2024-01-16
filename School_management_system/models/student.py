from odoo import api, fields, models, _

class StudentStudent(models.Model):
    _name = "student.student"
    _order = "name"
    _description = "Student"

    rollno= fields.Integer(string="Roll No")  
    name = fields.Char(string="Name", required=True)
    deperment = fields.Char(string="Deperment")
    district = fields.Char(string="District")
    age = fields.Integer(string="Age")
    gender = fields.Selection ([ 
        ('male', 'Male'),
        ('female', 'Female'),

    ])
    mark1= fields.Integer(string="Mark1", required= True)
    mark2= fields.Integer(string="Mark2", required= True)    
    #field_name = fields.Boolean(string="check box", default=False)
    isPassed = fields.Boolean(string="isPassed", compute="_compute_name", store=True)
    isFailed = fields.Boolean(string="isFailed")
    


    
    @api.depends('mark1', 'mark2')
    def _compute_name(self):
        print('inside compute')
        self.isPassed=False
        self.isFailed=False
        
        #print(total) 
        if self.mark1 and self.mark2:
            if self.mark1 + self.mark2 > 40:
                self.isPassed= True
            else:
                self.isFailed=True
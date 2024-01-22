

{
    'name': 'AManagement System',
    'version': '1.0.0',
    'category': 'Management',
    'author': 'Nasir Uddin',
    'summary': 'This is for all management system',
    'description': """
       This is for all management system
    """,
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        # 'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag.xml',
        'views/test.xml',
        'report/report.xml',
        'report/patient_card.xml',
        
    
    ],
    'demo': [],
    'application': True,
    'sequence': -100,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}


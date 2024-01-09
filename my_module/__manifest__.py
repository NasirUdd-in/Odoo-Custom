# my_module/__manifest__.py

{
    'name': 'My Modules',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Your Name',
    'summary': 'A simple Odoo module for managing tasks',
    'depends': ['base'],
    'data': [
        'views/task_view.xml',
    ],
    'installable': True,
    'application': True,
}

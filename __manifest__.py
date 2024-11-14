{
    'name': 'Student Management',
    'summary': "Student Management Software",
    'sequence': 10,
    'description': "Gestion des étudiants",
    'author': "OMAR ABARRA",
    'website': "https://odoo.com/app/Student_Management",
    'category': 'Students',
    'version': '2.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',  # Add this line
        'views/student.xml',
        'views/department_views.xml',
        'data/sequence.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
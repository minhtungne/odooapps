{
    'name': 'My Secure Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module đơn giản với bảo mật và điều hướng UI',
    'author': 'Tung',
    'depends': ['base'],
    'data': [
        'views/my_secure_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}

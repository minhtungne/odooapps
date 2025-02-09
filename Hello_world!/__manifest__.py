{
    'name': 'Hello, World!',
    'version': '1.0',
    'description': 'Module cơ bản phát triển trên Odoo.',
    'author': 'Minh Tung',
    'depends': [
        
        ],  
    'data': [ 
        'security/ir.model.access.csv',
        'views/test_model_1_views.xml',
        'views/test_model_1_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

{
    'name': 'Custom Sales Module',
    'version': '1.0',
    'depends': ['sale'],
    'author': 'Aya Berroulech',
    'category': 'Sales',
    'description': """
        Custom module for extending Sales Order functionality.
    """,
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'icon': 'module_icon.png',
}

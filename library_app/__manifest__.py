{
        'name': 'Library Management',
        'version': '12.0.1.0',
        'description': 'Manage library book catalogue and lending',
        'author': 'YUNFEN',
        'depends': ['base'],
        'application': True,
        'data': [
                'security/library_security.xml',
                'security/ir.model.access.csv',
                'views/library_menu.xml',
                'views/book_view.xml',
                'views/book_list_template.xml',
        ],
}

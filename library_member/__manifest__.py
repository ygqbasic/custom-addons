{
    'name': 'Library Members',
    'description': 'Manage people who will be able to borrow books.',
    'version': '12.0.1.0',
    'author': 'YUNFEN',
    'depends': ['library_app', 'mail'],
    'application': False,
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/member_view.xml',
        'views/book_list_template.xml',
    ]
}
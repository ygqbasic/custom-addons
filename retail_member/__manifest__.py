{
        'name': 'Retail CRM Member Center',
        'version': '12.0.1.0',
        'description': 'Manage retail members',
        'author': 'YUNFEN',
        'depends': ['base', 'mail'],
        'application': True,
        'data': [
                'security/member_security.xml',
                'security/ir.model.access.csv',
                'views/member_menu.xml',
                'views/member_view.xml',
                'views/member_list_template.xml',
                'views/member_account_view.xml',
        ],
}

# -*- coding: utf-8 -*-
{
    'name': "质检",

    'summary': """
        质检流程包括取号，报告基础信息，样品信息录入，安排测试项目等功能
        """,

    'description': """
        质检
    """,

    'author': "Guoqing Yang",
    'website': "https://www.yf-micro.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/lims_security.xml',
        'data/ir.sequence.xml',
        'data/lims_report_stage.xml',
        'security/ir.model.access.csv',
        'views/lims_menu.xml',
        'views/client_view.xml',
        'views/submitter_view.xml',
        'views/report_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'sequence':1,
}
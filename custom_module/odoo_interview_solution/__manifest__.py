# -*- coding: utf-8 -*-
{
    'name': "odoo_interview_solution",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'web_digital_sign'],

    # always loaded
    'data': [
        'security/access_groups.xml',
        'security/ir.model.access.csv',
        'views/purchase_order_view_inherit.xml',
        'views/res_users_view_inherit.xml',
        'report/purchase_order_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

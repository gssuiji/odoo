# -*- coding: utf-8 -*-
{
    'name': "library_checkout",

    'summary': """
       Members can borrow books from the library""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library_member'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/checkout_view.xml',
        'views/library_menu.xml',
        'data/library_checkout_stage.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'depends': ['library_member', 'mail'],

}

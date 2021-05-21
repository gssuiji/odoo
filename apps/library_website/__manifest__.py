# -*- coding: utf-8 -*-
{
    'name': "Library Website",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Create and check book checkout requests.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'library_checkout',
        'website',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/checkout_template.xml',
        'views/website_assets.xml',
        'views/helloworld_template.xml',
        'views/library_member.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

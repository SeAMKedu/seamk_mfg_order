# -*- coding: utf-8 -*-
{
    'name': "seamk_mfg_order",

    'summary': """
        Post manufacturing order data to MES application""",

    'description': """
        First, reads the name and quantity on the product to be manufactured.
        Then, posts the manufacturing order data to an external MES
        application, which handles the actual production process.
    """,

    'author': "seamk",
    'website': "https://www.seamk.fi/en/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False
}

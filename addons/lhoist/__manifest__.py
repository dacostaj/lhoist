# -*- coding: utf-8 -*-
{
    'name': "lhoist",

    'summary': """
        Modulo para la empresa Lhoist Colombia SAS""",

    'description': """
        Este es un modulo que le brinda a la empresa Lhoist Colombia SAS las funcionalidades
        de mantener un control a nivel de software de los mantenimientos de sus equipos
    """,

    'author': "Dickson Manuel Acosta Julio",
    'website': "http://www.net-technology.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
}
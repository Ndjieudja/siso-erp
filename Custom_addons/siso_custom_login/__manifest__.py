# -*- coding: utf-8 -*-
########################################################################################
#
#    SISO WEB based on Odoo, Open Source Management Solution
#    Copyright (C) 2023 (<http://ssolutionets.com>).
#    NDJIEUDJA GABRIEL < gabrielndjieudja@gmail.com | gabrieldjieudja@ssolutionets.com>
#
########################################################################################

{
    'name': "SISO CUSTOM LOGIN",

    'summary': """CUSTOM LOGIN ADMIN""",

    'description': """
        CUTOMISATION DU LOGIN AU COULEUR DE L'ENTREPRISE
    """,

    'author': 'NDJIEUDJA GABRIEL gabrielndjieudja@gmail.com',
    'website': "https://ssolutionets.com",
    'images': ['static/description/icon.png'],

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        #views
        'views/siso_custom_login.xml'
        
    ],

}

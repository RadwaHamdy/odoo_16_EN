# -*- coding: utf-8 -*-
{
    'name': "hr_appraisal_enhancement",
    'version': '1.0',
    'summary': """
        Appraisal customization""",

    'description': """
       adding new model competencies, updating goal model
    """,

    'author': "",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_appraisal'],

    # always loaded
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/hr_competencies_views.xml',
        'views/hr_appraisal_goal_view.xml',
        # 'data/res_config_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}

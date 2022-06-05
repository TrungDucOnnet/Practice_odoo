# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School WebLearn',
    'version' : '1.1',
    'summary': 'School Management System',
    'sequence': 1,
    'description': """
School Management System
    """,
    'category':'School',
    'depends': ['base'],
    'qweb': ['static/src/xml/btn_tree_mutil_update.xml'],
    'data': [
        'security/security_access_data.xml',
        'security/ir.model.access.csv',
        'data/school_data.xml',
        'wizard/views/batch_update.xml',
        'wizard/views/create_student.xml',
        'views/school_views/res_config_setting_view_form.xml',
        'views/school_views/school_view.xml',
    ],
    'demo': [
        # 'demo/demo.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'school_weblearn/static/src/js/bold.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Qweb report Examples',
    'version' : '1.1',
    'summary': '4 type of hook',
    'description': """
Qweb report Examples
    """,
    'category':'school',
    'depends': ['school_weblearn', 'student_weblearn'],
    'data': [
        'report/student_template_report.xml',
    ],
    'assets': {
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

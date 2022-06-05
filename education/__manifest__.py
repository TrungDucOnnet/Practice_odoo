# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'education System',
    'version' : '1.1',
    'summary': 'education System',
    'sequence': 10,
    'description': """
education System
    """,
    'depends': ['mail', 'website_sale'],
    'data': [
        # 'security/account_security.xml',
        'views/school_information.xml',
        'views/class_information.xml',
        'views/student_information.xml',
        'views/subject_information.xml',
        'security/ir.model.access.csv',
        'reports/school_report_template.xml',
        'views/school_report.xml',
        'views/templates.xml',
        # 'data/data.xml'
    ],
    'demo': [
        # 'demo/demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

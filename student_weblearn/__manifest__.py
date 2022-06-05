# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Student WebLearn',
    'version' : '1.1',
    'summary': 'Student Management System',
    'sequence': 1,
    'description': """
Student Management System
    """,
    'category':'Student',
    'depends': ['base','school_weblearn','mail'],
    'data': [
        'views/student_views/student_view.xml',
        'views/student_views/public_school_student_view.xml',
        'views/car_engine_views/car_engine_view.xml',
        'security/ir.model.access.csv',
        'wizard/students_fees_update_wizard_view.xml',
        'demo/hobby.csv',
        'demo/school.profile.csv',
        'demo/student.profile.csv',
        'data/student_data.xml',
        'data/delete_data.xml',
        # 'report/report.xml',
    ],
    'demo': [
        # 'demo/demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

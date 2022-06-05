# -*- coding: utf-8 -*-
{
    'name': 'Color Picker',
    'version': '1.1',
    'summary': 'Color Picker Widget for Integer Field',
    'sequence': 10,
    'description': 'DEMO ADDON',
    'category': 'Demo',
    'depends': ['web'],
    'data': [

    ],
    'assets': {
        'web.assets_backend': [
            'color_picker/static/src/js/components.js',
            'color_picker/static/src/scss/style.scss',
        ],
        'web.assets_qweb': [
            'color_picker/static/src/xml/templates.xml',
        ]
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

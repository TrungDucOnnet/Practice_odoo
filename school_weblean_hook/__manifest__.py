# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hook Examples',
    'version' : '1.1',
    'summary': '4 type of hook',
    'description': """
4 type of hook Tutorial
    """,
    'category':'Tutorial',
    'depends': ['contacts'],
    'data': [
    ],
    'assets': {
    },
    'pre_init_hook':'_weblearns_pre_init_hook',
    'post_init_hook':'_weblearns_post_init_hook',
    'uninstall_hook':'_weblearns_unistall_hook',
    'post_load':'_weblearns_post_load_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}

# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_address = fields.Text('Default School\'s Address', default_model='school.profile')
    schoolprofile_is_check_duplicated_name = fields.Boolean('Check Duplicated Pet Name', config_parameter='schoolprofile.is_check_duplicated_name')
# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)

class BatchUpdateWizard(models.TransientModel):
    _name = "school.batch_update.wizard"
    _description = "Batch update for school model"

    school_type = fields.Selection([('public', 'Public School'), ('private', 'Private School')], string='School Type')

    def multi_update(self):
        ids = self.env.context['active_ids']  # selected record ids
        schools = self.env["school.profile"].browse(ids)
        new_data = {}

        if self.school_type:
            new_data["school_type"] = self.school_type

        schools.write(new_data)

    @api.model
    def default_get(self, fields):
        res = super(BatchUpdateWizard, self).default_get(fields)
        res["school_type"] = 'public'
        return res

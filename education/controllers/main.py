# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):

    @http.route('/academy/academy/', auth='public',website=True)
    def index(self, **kw):
        Schools = http.request.env['school.information']
        return http.request.render('education.index', {
            'schools': Schools.search([])
        })

    @http.route('/academy/<model("school.information"):school>/', auth='public', website=True)
    def school(self, school):
        return http.request.render('education.biography', {
            'infor': school
        })
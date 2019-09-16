# -*- coding: utf-8 -*-
from odoo import http

# class LimsTestAssign(http.Controller):
#     @http.route('/lims_test_assign/lims_test_assign/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lims_test_assign/lims_test_assign/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lims_test_assign.listing', {
#             'root': '/lims_test_assign/lims_test_assign',
#             'objects': http.request.env['lims_test_assign.lims_test_assign'].search([]),
#         })

#     @http.route('/lims_test_assign/lims_test_assign/objects/<model("lims_test_assign.lims_test_assign"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lims_test_assign.object', {
#             'object': obj
#         })
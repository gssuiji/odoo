# -*- coding: utf-8 -*-
# from odoo import http


# class GsStaff(http.Controller):
#     @http.route('/gs_staff/gs_staff/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gs_staff/gs_staff/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gs_staff.listing', {
#             'root': '/gs_staff/gs_staff',
#             'objects': http.request.env['gs_staff.gs_staff'].search([]),
#         })

#     @http.route('/gs_staff/gs_staff/objects/<model("gs_staff.gs_staff"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gs_staff.object', {
#             'object': obj
#         })

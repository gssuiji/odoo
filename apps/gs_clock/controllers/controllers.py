# -*- coding: utf-8 -*-
# from odoo import http


# class GsClock(http.Controller):
#     @http.route('/gs_clock/gs_clock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gs_clock/gs_clock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gs_clock.listing', {
#             'root': '/gs_clock/gs_clock',
#             'objects': http.request.env['gs_clock.gs_clock'].search([]),
#         })

#     @http.route('/gs_clock/gs_clock/objects/<model("gs_clock.gs_clock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gs_clock.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
from odoo import http

# class Lhoist(http.Controller):
#     @http.route('/lhoist/lhoist/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lhoist/lhoist/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lhoist.listing', {
#             'root': '/lhoist/lhoist',
#             'objects': http.request.env['lhoist.lhoist'].search([]),
#         })

#     @http.route('/lhoist/lhoist/objects/<model("lhoist.lhoist"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lhoist.object', {
#             'object': obj
#         })
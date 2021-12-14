# -*- coding: utf-8 -*-
# from odoo import http


# class SeamkMfgOrder(http.Controller):
#     @http.route('/seamk_mfg_order/seamk_mfg_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seamk_mfg_order/seamk_mfg_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('seamk_mfg_order.listing', {
#             'root': '/seamk_mfg_order/seamk_mfg_order',
#             'objects': http.request.env['seamk_mfg_order.seamk_mfg_order'].search([]),
#         })

#     @http.route('/seamk_mfg_order/seamk_mfg_order/objects/<model("seamk_mfg_order.seamk_mfg_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seamk_mfg_order.object', {
#             'object': obj
#         })

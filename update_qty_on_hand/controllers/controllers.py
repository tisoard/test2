# -*- coding: utf-8 -*-
from odoo import http

# class UpdateQtyOnHand(http.Controller):
#     @http.route('/update_qty_on_hand/update_qty_on_hand/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_qty_on_hand/update_qty_on_hand/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_qty_on_hand.listing', {
#             'root': '/update_qty_on_hand/update_qty_on_hand',
#             'objects': http.request.env['update_qty_on_hand.update_qty_on_hand'].search([]),
#         })

#     @http.route('/update_qty_on_hand/update_qty_on_hand/objects/<model("update_qty_on_hand.update_qty_on_hand"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_qty_on_hand.object', {
#             'object': obj
#         })
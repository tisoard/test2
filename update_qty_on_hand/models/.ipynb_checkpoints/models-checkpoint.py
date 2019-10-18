# -*- coding: utf-8 -*-

from odoo import models, fields, api

class update_qty_on_hand(models.Model):
    _name = 'update_qty_on_hand.update_qty_on_hand'
    _inherit = 'product.product'
    _inherit = 'stock.inventory'

    # only keep records appearing in a bill of material (components, raw materials)
    if records.filter(lambda r: r.bom_line_ids!=False):
        inventory_quantity = 100


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
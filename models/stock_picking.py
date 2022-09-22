# -*- coding: utf-8 -*-




from odoo import models,fields,api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    client_order_ref = fields.Char(string='Customer Reference', copy=False)

    @api.model
    def create(self,vals):
        record = super(StockPicking, self).create(vals)
        if vals.get('backorder_id',False):
            client_order_ref = self.browse(vals['backorder_id']).client_order_ref
            record.write({'client_order_ref':client_order_ref})
        return record


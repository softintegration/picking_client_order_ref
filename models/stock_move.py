# -*- coding: utf-8 -*-




from odoo import models,fields,api


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        res = super()._get_new_picking_values()
        client_order_refs = self.filtered(lambda m: m.sale_line_id).mapped('sale_line_id').mapped("order_id").mapped("client_order_ref")
        if len(client_order_refs) == 0:
            client_order_ref = False
        else:
            client_order_ref = ','.join(client_order_refs[:5])
            if len(client_order_refs) > 5:
                client_order_ref += "..."
        if res:
            res.update({'client_order_ref':client_order_ref})
        return res



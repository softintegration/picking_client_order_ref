# -*- coding: utf-8 -*-




from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"


    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()
        self.mapped("picking_ids").write({'client_order_ref':self.client_order_ref})
        return res

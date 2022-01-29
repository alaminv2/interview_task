from odoo import models, fields


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    flag_invisible = fields.Boolean(default=False)
    flag_invisible_md = fields.Boolean(default=False)

    def button_confirm(self):
        for order in self:
            if order.state not in ['draft', 'sent']:
                continue
            order._add_supplier_to_product()
            if order.amount_total > 50000:
                order.flag_invisible = True
            else:
                order.flag_invisible_md = True
            order.write({'state': 'to approve'})
        return True

    def print_po(self):
        print('Print PO', self.id)
        return self.env.ref('odoo_interview_solution.report_signatured_purchase_order').report_action(self)


class PurchaseOrderLineInherit(models.Model):
    _inherit = 'purchase.order.line'

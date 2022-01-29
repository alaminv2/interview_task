from odoo import models, api


class ReportMultplePurchase(models.AbstractModel):
    _name = 'report.odoo_interview_solution.report_multiple_purchase'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('dara = ', data)
        start_date = data['start_date']
        end_date = data['end_date']
        purcahse = self.env['purchase.order'].search([('date_order', '>=', start_date), ('date_order', '<=', end_date)])
        print(purcahse)
        return {
            'orders': purcahse
        }
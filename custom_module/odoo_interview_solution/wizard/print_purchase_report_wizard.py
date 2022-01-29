from odoo import models, fields
import datetime


class PrintPOReport(models.TransientModel):
    _name = 'print.purchase.report.wizard'

    start_date = fields.Date(string='Start Date', default=datetime.date.today())
    end_date = fields.Date(string='End Date', default=datetime.date.today())

    def print_po(self):
        data = self.read()[0]
        return self.env.ref('odoo_interview_solution.report_multiple_purchase_order').report_action(self, data=data)
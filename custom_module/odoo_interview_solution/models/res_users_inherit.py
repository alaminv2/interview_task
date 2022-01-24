from odoo import models, fields


class ResUserInherit(models.Model):
    _inherit = 'res.users'

    signature = fields.Binary(string='Signature')
from odoo import fields, models
from odoo.exceptions import Warning

class Client(models.Model):
    _name = 'lims.client'
    _description = 'Client'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    active = fields.Boolean('Active?', default=True)
    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True)
    
from odoo import fields, models
from odoo.exceptions import Warning

class Member(models.Model):
    _name = 'retail.member'
    _description = 'Member'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    active = fields.Boolean('Active?', default=True)
    distinct_number =  fields.Char()
    card_number = fields.Char()
    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True)
    member_account_ids = fields.One2many(
    'retail.member.account',
    'member_id',
    string='Third Party Accounts',)
    
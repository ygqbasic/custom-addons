from odoo import fields, models
from odoo.exceptions import Warning

class Account(models.Model):
    _name = 'retail.member.account'
    _description = 'Third Party Account'
    active = fields.Boolean('Active?',default=True)
    code = fields.Char()
    account_type = fields.Selection(
        [('openid', 'OpenId'),
        ('alipayid', 'AlipayId'),
        ('unionid', 'UnionId'),
        ('mobile', 'Mobile'),
        ('email', 'Email'),
        ]
    )
    follow_time = fields.Datetime(default=lambda s: fields.Datetime.now())
    member_id =  fields.Many2one(
        'retail.member',
        required=True,
    )
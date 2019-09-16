from odoo import fields, models

class ReportStage(models.Model):
    _name = 'lims.report.stage'
    _description = 'Report Stage'
    _order = 'sequence,name'

    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('new', 'New'),
        ('enter', 'Entered'),
        ('open', 'Asigned'),
        ('done', 'Completed'),
        ('cancel', 'Cancelled')],
        default='new',
    )
    
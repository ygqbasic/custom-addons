# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api

class Report(models.Model):
    _name = 'lims.report'
    _description = 'Report'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    active = fields.Boolean('Active?', default=True)
    name =  fields.Char(index=True,copy=False)
    _sql_constraints = [('report_number_uniq', 'unique(report_number)', 'Report Number Unique')]
    inspection_type = fields.Selection(
        [('self-check', 'Self check'),
        ('spot-check', 'Spot check'),
        ],track_visibility='onchange',
    )

    test_type = fields.Selection(
        [('product', 'Product Standard'),
        ('method', 'With Method'),
        ]
    )   

    inspection_cycle = fields.Selection(
        [(7, '7 days'),
        (5, '5 days'),
        (3, '3 days'),
        (2, '2 days'),
        ],default=7,track_visibility='always'
    ) 
    sampling_date = fields.Date(default=lambda s: fields.Date.today())
    inspection_due_date = fields.Date(compute="_compute_inspection_due_date", store=True)
    department_id = fields.Many2one(
        'hr.department',
        required=True)

    submitter_id = fields.Many2one(
    'lims.submitter',
    required=True,track_visibility='onchange',)

    client_id = fields.Many2one(
    'lims.client',
    required=True,track_visibility='onchange',)
    
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    sample_level = fields.Selection(
        [('a', 'Level A'),
        ('b', 'Level B'),
        ('c', 'Level C'),
        ('first', 'First Level'),
        ('second', 'Second Level'),
        ('standard', 'Standard'),
        ],required=True
    )   
    sample_description = fields.Char(required=True,track_visibility='onchange',)
    sample_quantity = fields.Integer(required=True,track_visibility='onchange',)
    sample_model = fields.Char(track_visibility='onchange',)
    sample_sku = fields.Char(track_visibility='onchange',)
    sample_brand = fields.Char(track_visibility='onchange',)


    @api.model
    def _default_stage(self):
        Stage = self.env['lims.report.stage']
        return Stage.search([], limit=1)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    stage_id = fields.Many2one(
        'lims.report.stage',
        default=_default_stage,
        group_expand='_group_expand_stage_id',track_visibility='always',
    )
    state = fields.Selection(related='stage_id.state')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = self.env['ir.sequence'].next_by_code('lims.report.code') or '/'
        return super(Report, self).create(vals)

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

    @api.depends('inspection_cycle')
    def _compute_inspection_due_date(self):
        duration = timedelta(days=self.inspection_cycle, seconds=-1)
        self.inspection_due_date = fields.Date.today() + duration

class ReportSample(models.Model):
    _name = 'lims.report.sample'
    _description = 'Samples'
    name = fields.Char()
    



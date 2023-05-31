from odoo import api, fields, models


class HrAppraisalGoalEnhancement(models.Model):
    _inherit = 'hr.appraisal.goal'

    period = fields.Integer(string='Period')
    period_from = fields.Date(string='From')
    period_to = fields.Date(string='to')
    objective_id = fields.One2many(comodel_name="hr.objective", inverse_name="goal_id",
                                   string="Objective",
                                   required=False)

    @api.onchange('period_from', 'period_to')
    def onchange_from_to(self):
        if self.period_from and self.period_to:
            self.period = (self.period_to + self.period_from).days


class HrCompetencies(models.Model):
    _name = 'hr.objective'

    name = fields.Char(string='Objective')
    weight = fields.Selection(string='Weight', selection=[
        ('zero', '0%'),
        ('twentyfive', '25%'),
        ('fifty', '50%'),
        ('seventyfive', '75%'),
        ('hundred', '100%')])
    goal_id = fields.Many2one(comodel_name='hr.appraisal.goal', string='Parent')

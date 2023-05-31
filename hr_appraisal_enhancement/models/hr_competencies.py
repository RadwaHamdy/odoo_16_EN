import datetime
from odoo import models, fields, api, exceptions


class HrCompetencies(models.Model):
    _name = 'hr.competencies'

    name = fields.Char(string="Competency Name")
    description = fields.Text(string="Competency Description")
    hr_competencies_lines = fields.One2many(comodel_name="hr.competencies.line", inverse_name="competency_id",
                                            string="Competency Lines",
                                            required=False)


class HrCompetenciesLine(models.Model):
    _name = 'hr.competencies.line'

    line_description = fields.Char(string='Description')
    level = fields.Selection(string='Level', selection=[
        ('basic', 'Basic'),
        ('competent', 'Competent'),
        ('advanced', 'Advanced')])
    competency_id = fields.Many2one(comodel_name='hr.competencies', string='Competency')

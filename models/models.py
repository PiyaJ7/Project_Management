from odoo import models, fields

class Project(models.Model):
    _name = 'project.management'
    _description = 'Project Management'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

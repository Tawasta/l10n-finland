# -*- coding: utf-8 -*-

from odoo import fields, models


class ResMunicipality(models.Model):
    _name = 'res.municipality'
    _description = 'Municipality'
    _order = 'code'

    name = fields.Char(
        string='Municipality Name', required=True, translate=True, help='The full name of the municipality.')
    short_name = fields.Char(
        string='Short Name', required=True, translate=True, help='The short name of the municipality.')
    code = fields.Char(
        string='Code', required=True, size=3)
    description = fields.Char(
        string="Description",
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the municipality must be unique !'),
        ('code_uniq', 'unique (code)',
            'The code of the municipality must be unique !')
        ('short_name_uniq', 'unique (short_name)',
            'The short name of the municipality must be unique !')
    ]

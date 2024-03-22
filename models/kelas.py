from odoo import api, fields, models, _


class Kelas(models.Model):
    _name = 'kelas'
    _description = 'Kelas'

    name = fields.Char(string='Name')

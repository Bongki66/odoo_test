from odoo import api, fields, models, _


class MataPelajaran(models.Model):
    _name = 'mata.pelajaran'
    _description = 'Mata Pelajaran'

    name = fields.Char(string='Name')

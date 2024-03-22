from odoo import api, fields, models, _


class Guru(models.Model):
    _name = 'guru'
    _description = 'Guru'

    name = fields.Char(string='Name')
    mapel_id = fields.Many2one('mata.pelajaran', string='Mata Pelajaran')

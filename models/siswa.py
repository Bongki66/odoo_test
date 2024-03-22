from odoo import api, fields, models, _


class Siswa(models.Model):
    _name = 'siswa'
    _description = 'Siswa'

    name = fields.Char(string='Name')
    date_of_birth = fields.Date(string='Date of Birth')
    kelas_id = fields.Many2one('kelas', string='Kelas')
    guru_id = fields.Many2one('guru', string='Guru')
    mapel_id = fields.Many2one(related='guru_id.mapel_id', store=True)

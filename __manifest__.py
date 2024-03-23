# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Siswa',
    'version': '1.1',
    'summary': 'Siswa',
    'sequence': 10,
    'description': """""",
    'images': [],
    'depends': ['base'],
    'data': [
        # security
        'security/ir.model.access.csv',

        # views
        'views/siswa_views.xml',
        'views/guru_views.xml',
        'views/mapel_views.xml',
        'views/kelas_views.xml',

        # reports
        'report/siswa_report_templates.xml',
        'report/siswa_report.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

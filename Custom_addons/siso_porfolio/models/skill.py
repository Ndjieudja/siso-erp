# --*-- encoding:utf8 --*--

from odoo import models, fields

class SisoSkill(models.Model):
    _name = "siso.skill"
    _description = "Compétence"

    name = fields.Char(
        required=True,
        string="Name"
    )

    level = fields.Selection(
        [
            ('beginner', 'Débutant'),
            ('intermediate', 'Intermédiaire'),
            ('advanced', 'Avancé')
        ], 
        default='intermediate'
    )
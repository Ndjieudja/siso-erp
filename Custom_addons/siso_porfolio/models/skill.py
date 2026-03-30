# -*- coding: utf-8 -*-
####################################################################################
#
#    SISO WEB based on Odoo, Open Source Management Solution
#    Copyright (C) 2023 (<https://ssolutionets.com).
#    Martial MBE < gabrielndjieudja@gmail.com | gabrielndjieudja@ssolutionets.com >
#    See LICENSE file for full copyright and licensing details.
#
####################################################################################


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
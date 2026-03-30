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

class SisoProject(models.Model):
    _name = "siso.project"
    _description = "Projet Portfolio"

    name = fields.Char(
        required=True,
        string="Name",
    )

    description = fields.Text(
        string="Description",
    )

    image = fields.Binary(
        attachment=True,
        string="Image",
    )

    link = fields.Char(
        string="Lien"
    )

    date = fields.Date(
        string="Date"
    )

    technologies = fields.Char(
        string="Technologie"
    )
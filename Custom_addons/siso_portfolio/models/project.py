# --*-- encoding:utf8 --*--

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
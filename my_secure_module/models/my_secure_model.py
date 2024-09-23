from odoo import models, fields

class MySecureModel(models.Model):
    _name = 'my.secure.model'
    _description = 'Secure Model for Demo'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)

<<<<<<< HEAD
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelloWorld(models.Model):
    _name = 'hello_world'
    _description = 'Hello World module'

    name = fields.Char(string='Text to display', required=True)
=======
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelloWorld(models.Model):
    _name = 'hello_world'
    _description = 'Hello World module'

    name = fields.Char(string='Text to display', required=True)
>>>>>>> a9064aa5d1392ebad5de6625748eec7cd0146484

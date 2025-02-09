from odoo import fields, models

class TestModel(models.Model):
    _name = "test_model"
    _description = "Test Model"
    
    name = fields.Char(
        string='name',
        required=True,
        tracking=True,
    )
    description = fields.Text(
        string='description',
    )
    postcode = fields.Char(
        string='postcode',
    )
    date_availability = fields.Date(
        string='date_availability',
        default=fields.Date.context_today,
        copy=False,
    )
    expected_price = fields.Float(
        string='expected price',
        required=True,
    )
    selling_price = fields.Float(
        string='selling_price',
        readonly=True,
        copy=False,
    )
    bedrooms = fields.Integer(
        string='bedrooms',
        default='2',
    )
    living_area = fields.Integer(
        string='living_area',
    )
    facades = fields.Integer(
        string='facades',
    )
    garage = fields.Boolean(
        string='garage',
    )
    garden = fields.Boolean(
        string='garden',
    )
    garden_area = fields.Integer(
        string='garden_area',
    )
    garden_orientation = fields.Selection(
        string='garden_orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
    )
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold ', 'Sold '), ('canceled', 'Canceled')],
        required=True,
        copy=False,
        default='new',
    )
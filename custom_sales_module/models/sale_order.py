from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_instructions = fields.Text(
        string='Delivery Instructions',
        help='Provide any specific instructions for delivery.',
        required=False,
        readonly=False,
        translate=True,
    )
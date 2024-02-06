from odoo.tests.common import TransactionCase

class TestSaleOrder(TransactionCase):
    def test_delivery_instructions_field_exists(self):
        sale_order_model = self.env['sale.order']
        sale_order = sale_order_model.create({
            'name': 'Test Sale Order',
            'partner_id': self.env.ref('base.res_partner_2').id,
        })
        self.assertTrue('delivery_instructions' in sale_order._fields)
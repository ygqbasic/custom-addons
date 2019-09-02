from odoo.tests.common import TransactionCase
 
class TestMember(TransactionCase):
    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)
        self.Member = self.env['retail.member']
        self.member_ode = self.Member.create({
            'card_number': '9999999999'
            })
        return result
    def test_create(self):
        "Test Books are active by default"
        self.assertEqual(self.member_ode.active, True)

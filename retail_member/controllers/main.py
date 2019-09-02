from odoo import http
 
class Members(http.Controller):
 
    @http.route('/rettail/members', auth='user')
    def list(self, **kwargs):
        Member = http.request.env['retail.member']
        members = Member.search([])
        return http.request.render(
            'retail_member.member_list_template', {'members':books})
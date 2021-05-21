from odoo import http


class Staff(http.Controller):

    @http.route('/gs/staff', auth='user')
    def list(self, **kwargs):
        Staff = http.request.env['gs.staff']
        staffs = Staff.search([])
        return http.request.render(
            'gs_staff.staff_list_template', {'staffs': staffs}
        )

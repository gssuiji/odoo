from odoo import fields, models
from odoo.exceptions import Warning


class Clock(models.Model):
    _name = 'gs.clock'
    _description = 'Clock'
    staff_id = fields.Many2one(
        'gs.staff',
        required=True
    )
    clock_in = fields.Date("上班时间")
    clock_out = fields.Date("下班时间")

    def button_up(self):
        raise Warning("上班打卡成功")

    def button_out(self):
        raise Warning("下班打卡成功")

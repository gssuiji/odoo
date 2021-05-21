from odoo import fields, models


class CheckoutStage(models.Model):
    _name = 'library.checkout.stage'
    _description = 'Checkout Stage'
    _order = 'sequence,name'
    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('new', 'New'),
         ('open', 'Borrowed'),
         ('done', 'Returned'),
         ('cancel', 'Cancelled')],
        default='new',
    )

    def button_done(self):
        # 查找 done 阶段的记录,设置其 stage_id 值为完成阶段
        Stage = self.env['library.checkout.stage']
        done_stage = Stage.search(
            [('state', '=', 'done')],
            limit=1)
        for checkout in self:
            checkout.stage_id = done_stage
        return True

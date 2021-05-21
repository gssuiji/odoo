from odoo import fields, models
from odoo.exceptions import Warning


class Staff(models.Model):
    _name = 'gs.staff'
    _description = 'Staff'
    name = fields.Char('姓名', require=True)
    sex = fields.Char('性别')
    date_onboarding = fields.Date('入职时间')
    image = fields.Binary('头像')
    author_ids = fields.Many2many('res.partner', string='Authors')

    def button_check_name(self):
        if self.name:
            if len(self.name)>1:
                # print(f"type:{self.name},name:{self.name}")
                return None
            else:
                raise Warning('name长度必须大于1')
            return None
        else:
            raise Warning("name不能为空")

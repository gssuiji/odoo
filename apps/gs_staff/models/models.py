# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gs_staff(models.Model):
#     _name = 'gs_staff.gs_staff'
#     _description = 'gs_staff.gs_staff'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import api, fields, models
from odoo.exceptions import Warning


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')# 图书编号
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is an invalid ISBN' % book.isbn)
        return True

    def _check_isbn(self):
        self.ensure_one()
        isbn = self.isbn.replace('-', '')  # 为保持兼容性 Alan ⾃⾏添加
        digits = [int(x) for x in isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def _check_isbn(self):
        self.ensure_one()
        isbn = self.isbn.replace('-', '')
        digits = [int(x) for x in isbn if x.isdigit()]
        if len(digits) == 10:
            ponderators = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            total = sum(a * b for a, b in zip(digits[:9], ponderators))
            check = total % 11
            return digits[-1] == check
        else:
            return super()._check_isbn()
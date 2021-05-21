from odoorpc import ODOO


class LibraryAPI():
    def __init__(self, srv, port, db, user, pwd):
        self.api = ODOO(srv, port=port)
        self.api.login(db, user, pwd)
        self.uid = self.api.env.uid
        self.model = 'library.book'
        self.Model = self.api.env[self.model]

        def execute(self, method, arg_list, kwarg_dict=None):
            return self.api.execute(
                self.model,
                method, *arg_list, **kwarg_dict)

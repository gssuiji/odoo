from xmlrpc import client


class LibraryAPI():
    """
    存储了所有创建执⾏模型调⽤的对象的所有信息：API引⽤、uid、密码、数据库名
    和要使⽤的模型。接下来我们定义⼀个帮助⽅法来执⾏调⽤。有赖于前⾯对象存储的数据该
    ⽅法可以很精炼
    """

    def __init__(self, srv, port, db, user, pwd):
        common = client.ServerProxy(
            'http://%s:%d/xmlrpc/2/common' % (srv, port))
        self.api = client.ServerProxy(
            'http://%s:%d/xmlrpc/2/object' % (srv, port))
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = 'library.book'

    def execute(self, method, arg_list, kwarg_dict=None):
        # 接收⼀个可选的 ID 列表来获取数据。如果没传⼊数据，则返回所有记录
        return self.api.execute_kw(
            self.db, self.uid, self.pwd, self.model,
            method, arg_list, kwarg_dict or {})

    def search_read(self, text=None):
        domain = [('name', 'ilike', text)] if text else []
        fields = ['id', 'name']
        return self.execute('search_read', [domain, fields])

    def create(self, title):
        # ⽤于创建给定书名的新书并返回所创建记录的 ID
        vals = {'name': title}
        return self.execute('create', [vals])

    def write(self, title, id):
        # 传⼊新书名和图书 ID 作为参数，并对该书执⾏写操作
        vals = {'name': title}
        return self.execute('write', [[id], vals])

    def unlink(self, id):
        # 根据id删除数据
        return self.execute('unlink', [[id]])


if __name__ == '__main__':
    # 测试配置
    srv, db, port = 'localhost', 'odoo14', 8069
    user, pwd = 'admin', 'admin'
    api = LibraryAPI(srv, port, db, user, pwd)

    from pprint import pprint

    pprint(api.search_read())

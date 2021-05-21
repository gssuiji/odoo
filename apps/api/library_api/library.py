from argparse import ArgumentParser
from .library_api import LibraryAPI

parser = ArgumentParser()
parser.add_argument('command', choices=['list', 'add', 'set-title', 'del'])
parser.add_argument('params', nargs='*') # 可选参数
args = parser.parse_args()
# ⾸先为 Odoo服务准备连接
srv, port, db = 'localhost', 8069, 'odoo14'
user, pwd = 'admin', 'admin'
api = LibraryAPI(srv, port, db, user, pwd)
# list命令来列出图书
if args.command == 'list':
    text = args.params[0] if args.params else None
    books = api.search_read(text)
    for book in books:
        print('%(id)d %(name)s' % book)

# 添加add命令，这⾥使⽤了额外的书名作为参数
if args.command == 'add':
    for title in args.params:
        new_id = api.create(title)
        print('Book added with ID %d.' % new_id)

# set-title命令允许我们修改已有图书的书名，应传⼊两个参数，新的书名和图书的 ID
if args.command == 'set-title':
    if len(args.params) != 2:
        print("set command requires a title and ID.")
    else:
        book_id, title = int(args.params[0]), args.params[1]
        api.write(title, book_id)
        print('Title set for Book ID %d.' % book_id)

# 实现 del 命令来删除图书记录
if args.command == 'del':
    for param in args.params:
        api.unlink(int(param))
        print('Book with ID %s deleted.' % param)







# -*-coding:utf-8-*-

from db import DBHelper
from item import UserItem

# 测试案例
db_ = DBHelper()
print(db_.exist('user', 1))

item = UserItem(1, 'lili', '14', 'xiha', 'http://')
db_.save()

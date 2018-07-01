# -*-coding:utf-8-*-
import pymysql

import settings


# shift+F6重构
class DBHelper():
    def __init__(self):
        self.db = pymysql.connect(**settings.DATABASE.get('default'))  # **将字典对象变成关键参数传值
        self.cursor = self.db.cursor()

        '''  conn = pymysql.connect(
                                     host="10.35.0.128",     # 需要连接的主机的ip
                                     user="root",            # 用户名
                                     password="root",        # 密码
                                     db="bankstore",         # 选择操作的数据库
                                     port=3306)              # mysql的端口号
         '''

    def save(self, item):
        if self.exist('user', item.id):
            return
        try:
            self.cursor.execute('insert user(id,name,age,img,home) value(%s,%s,%s,%s,%s)',
                                args=(item.id,
                                      item.name,
                                      item.age,
                                      item.img,
                                      item.home))
            if self.cursor.rowcount:
                self.db.commit()  # 提交事务
                print(item.name, '数据库保存成功！！！')
        except:
            self.db.rollback()

    def exist(self, tableName, id):
        self.cursor.execute('select id from {} where id=%s'.format(tableName), args=(id))
        self.cursor.fetchone()  # fetchone拿到一个查询结果  fetchall 拿到可迭代对象
        return self.cursor.rowcount >= 1

    def close(self):
        self.db.close()  # 关闭数据库

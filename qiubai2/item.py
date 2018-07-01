# -*-coding:utf-8-*-

class UserItem():
    def __init__(self, id, name, age, img, home):
        self.id = id
        self.name = name
        self.age = age
        self.img = img
        self.home = home

    def __str__(self):
        return 'id:{},name:{},age:{},img"{},home:{}'.format(
                self.id,
                self.name,
                self.age,
                self.img,
                self.home)

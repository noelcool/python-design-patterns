import pymysql


class SingletonCreater(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance


class Database(SingletonCreater):
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(host='127.0.0.1', port=3307, user='root', password='123456', db='test',
                                              charset='utf8mb4')
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        return self.cursor


if __name__ == '__main__':
    Database()
    d1 = Database().connect()
    print(Database())
    print(Database())
    d1.execute('select * from cart')
    print(d1.fetchall())
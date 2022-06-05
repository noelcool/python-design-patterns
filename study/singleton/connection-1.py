import pymysql, copy


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = 3307
        self.__user = 'root'
        self.__password = '123456'
        self.__db_name = 'test'
        self.connection = None
        self.cursor = None

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(host=self.__host, port=self.__port, user='root', password=self.__password,
                                              db=self.__db_name, charset='utf8mb4')
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        return self.cursor


class Execute:
    @staticmethod
    def select(cursor, query, args={}):
        cursor.execute(query, args)


if __name__ == '__main__':
    # 커넥션 2개를 만들어서 출력해본다
    d1 = DataBase().connect()
    d2 = DataBase().connect()

    # <pymysql.cursors.DictCursor object at 0x10b9f5730> <pymysql.cursors.DictCursor object at 0x10b9f5730>
    print(d1, d2)

    d = DataBase()
    d.host = 'localhost'
    d1 = d.connect()
    Execute().select(d1, "select * from cart")
    print(d1.fetchall())
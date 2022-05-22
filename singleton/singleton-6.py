# 데이터베이스 기반 어플리케이션 싱글톤 패턴 적용

import sqlite3


class Metasingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):  # __call__ 파이썬 메서드를 사용해서 싱글톤 생성
        if cls not in cls._instances:
            cls._instances[cls] = super(Metasingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Metasingleton):  # Metasingleton 메타클래스의 도움으로 싱글톤 역할을 해서 한개의 database 클래스 객체만 생성
    connection = None
    cursor_obj = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor_obj = self.connection.cursor()
        return self.cursor_obj


db1 = Database().connect()
db2 = Database().connect()


"""
연산을 요청할때마다 database 클래스를 생성하지만 내부적으로는 한개의 객체만 생성, 데이터베이스의 동기화 보장
리소스를 적게 사용해 메모리와 CPU의 사용량을 최적화 할 수 있다
"""


print(db1)
print(db2)

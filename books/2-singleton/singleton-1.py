""""
글로벌하게 접근 가능한 단 한개의 객체만을 허용하는 패턴
동일한 리소스에 대한 동시 요청의 충돌을 막기 위해 한개의 인스턴스만 필요한 경우에 사용
데이터의 일관성 유지를 위해 DB에 작업을 수행하는 한개의 데이터베이스 객체가 필요한 경우
여러 서비스의 로그를 한개의 로그 파일에 순차적으로 동일한 로깅 객체를 사용해 남기는 경우

생성자를 private로 선언하고 객체를 초기화하는 static 함수를 만들면 간단하게 구현이 가능
첫 호출에 객체가 생성되고 클래스는 동일한 객체를 계속 리턴
"""


# 생성
class Singleton(object):
    def __new__(cls):  # override
        if not hasattr(cls, 'instance'):  # cls 객체가 instance 속성을 가지고 있는지 확인
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s1 = Singleton()
print("create1", s1)

s2 = Singleton()
print("create2", s2)

"""
create1 <__main__.Singleton object at 0x110328d00>
create2 <__main__.Singleton object at 0x110328d00>
"""
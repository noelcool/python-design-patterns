# 게으른 초기화
"""
인스턴스가 꼭 필요할 때 생성
사용할 수 있는 리소스가 제한적인 상황일 때 객체가 꼭 필요한 시점에 생성
"""


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("instance already created", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton()
print("create", s1.get_instance())

s2 = Singleton()

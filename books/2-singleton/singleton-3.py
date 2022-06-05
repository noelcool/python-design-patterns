# 모노스테이트 패턴

class Borg:
    __shared_state = {"1": "2"}  # 클래스 변수

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state  # 클래스 내 모든 객체의 상태 저장
        pass


b1 = Borg()
b2 = Borg()
b1.x = 4

print(b1)  # b1
print(b2)  # b2
print(b1.__dict__)  # b1, b2는 상태를 공유함
print(b2.__dict__)

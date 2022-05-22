# 메타클래스

class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("MyInt", args)
        return type.__call__(cls, *args, **kwargs)  # 이미 존재하는 클래스의 객체를 생성할 떄 호출되는 특수 메서드


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4, 5)  # MyInt 메타클래스의 __call__이 호출된다c3

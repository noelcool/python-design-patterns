# Adaptee (source) interface
class UserInterface:
    def user_id(self): pass

    def user_name(self): pass

    def card_id(self): pass


# Adaptee
class Socket(UserInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Target interface
class CardInterface:
    def card_id(self): pass

    def card_name(self): pass

    def card_company(self): pass


# The Adapter
class Adapter(UserInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


# Client
class ElectricKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire")
        else:
            if self.__power.live() == 1 and \
                    self.__power.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power")


def main():
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    # Make coffee
    kettle.boil()

    return 0


if __name__ == "__main__":
    main()

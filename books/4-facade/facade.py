"""
client : 결혼하는 당사자
4-facade : 웨딩플래너
subsystem : 음식, 호텔, 꽃 등의 업체
"""


class EventManager(object):  # 4-facade
    def __init__(self):
        self.musician = None
        self.caterer = None
        self.florist = None
        self.hotelier = None
        print("Event Manager :: Let me talk to the folks \n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier(object):  # subsystem
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    @staticmethod
    def __isAvailable():
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking \n")


class Florist(object):  # subsystem
    def __init__(self):
        print("Flower Decoration for the Event? --")

    @staticmethod
    def setFlowerRequirements():
        print("Carnations, Roses and Lilies would be used for Decorations \n")


class Caterer(object):  # subsystem
    def __init__(self):
        print("Foot Arrangements for the Event? --")

    @staticmethod
    def setCuisine():
        print("Chinese & Continental Cuisine to be served \n")


class Musician(object):  # subsystem
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    @staticmethod
    def setMusicType():
        print("Jazz and Classical will be played \n")


class You(object):  # client
    def __init__(self):
        print("You:: Whoa! Marrage Arrangements??")

    @staticmethod
    def askEventManager():
        print("You:: Let's Contact the Event Manager \n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")


you = You()
you.askEventManager()
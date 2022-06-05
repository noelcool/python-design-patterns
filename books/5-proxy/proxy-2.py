"""
You
현금 카드
클라이언트 - You
make_payment() - 셔츠를 결제, 내부적으로 Proxy의 메서드를 호출해 금액을 지불
__init__() - 프록시를 호출하고 생성
결제 성공시 __del__() 메서드를 호출
"""


class You:
    def __init__(self):
        print("YOU :: let buy the shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("YOU :: denim shirt is mine")
        else:
            print("YOU :: i should earn more")


"""
Payment(Subject)
Proxy와 RealSubject가 구현하는 인터페이스
Payment 클래스가 Subject에 해당, 추상 기본 클래스이며 인터페이스
Payment 클래스는 Proxy와 RealSubject가 구현해야 할 do_pay() 메서드를 포함
"""

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass


"""
Bank(RealSubject)
You의 계좌에서 판매자의 계좌로 돈을 인출한다
금액을 지불하는 여러 메서드가 있으나 setCard() 메서드를 사용해 카드 정보를 은행에 전달
__getAccount() 메서드는 카드 소지자의 계좌 정보를 조회하는 Bankq의 내부 메서드(카드번호와 계좌번호는 동일)
해당 계좌에 셔츠를 구입하기에 충분한 돈이 있는지 확인하는 __hasFunds() 메서드가 있다
판매자에게 지불하는 역할을 하는 do_pay() 메서드는 Bank 클래스에 구현
"""


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("BANK :: checking if account", self.__getAccount(), "has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("BANK :: paying the merchant")
            return True
        else:
            print("BANK :: not enough funds")
            return False


"""
DebitCard(Proxy)
결제 요청시 do_pay() 메서드를 호출
DebitCard 클래스는 RealSubject인 Bank의 대리 객체
payWithCard() 메서드는 내부적으로 RealSubject인 Bank클래스를 생성하고 카드 정보를 Bank에 전달
Bank클래스는 계좌를 확인하고 금액을 지불
"""


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("PROXY :: punch in card number : ")
        self.bank.setCard(card)
        return self.bank.do_pay()


you = You()
you.make_payment()

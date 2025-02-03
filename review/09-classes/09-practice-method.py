# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현


class BankAccount:
    # 클래스 변수
    interest_rate = 0.02  # 이자율

    # 생성자 메서드
    def __init__(self, owner, balance=0):
        # 인스턴스 변수
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금 (인스턴스 메서드)
    def deposit(self, amount):
        self.balance += amount
        print('입금이 완료되었습니다.')

    # 출금 (인스턴스 메서드) - 조건문도 함께 작성 (출금 가능한 경우가 존재함.)
    def withdraw(self, amount):
        if self.balance < amount:
            print('잔액이 부족합니다.')
        else:
            self.balance -= amount
            print('출금이 완료되었습니다.')

    # 이자율 설정
    @classmethod    # 클래스 메서드
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    # 금액이 양수인지 검증
    @staticmethod   # 스태틱 메서드
    def is_positive(amount):
        return amount > 0


# 계좌 개설 (인스턴스 생성)
my_account = BankAccount('Alice', 1000)
print(my_account.owner, my_account.balance)

# 입금 및 출금 (인스턴스 메서드 호출)
my_account.deposit(1000)
print(my_account.balance)

my_account.withdraw(500)
print(my_account.balance)

# 잔액 확인 (인스턴스 변수 참조)
print(my_account.balance)

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)
print(BankAccount.interest_rate)  # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
print(BankAccount.is_positive(my_account.balance))  # True

# 인스턴스 메서드 활용

class Counter:
    # 생성자 메서드
    def __init__(self):
        # 인스턴스 변수
        self.count = 0

    # 인스턴스 메서드
    def increment(self):
        self.count += 1


c = Counter()
print(c.count)
c.increment()
print(c.count)

# c2 생성해서 count 확인하기
c2 = Counter()
print(c2.count)
c.increment()
print(c.count, c2.count)
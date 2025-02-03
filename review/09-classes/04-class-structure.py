# 클래스 구성요소 확인하기

class Circle:
    # 클래스 변수
    pi = 3.14

    # 생성자 메서드
    def __init__(self, radius):
        # 인스턴스 변수수
        self.radius = radius

# 인스턴스 생성
c1 = Circle(1)
c2 = Circle(2)

# 인스턴스 변수(속성)
print(c1.radius)
print(c2.radius)

# 클래스 변수(속성)
print(c1.pi)
print(c2.pi)

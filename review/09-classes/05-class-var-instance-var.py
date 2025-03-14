class Circle:
    # 클래스 변수
    pi = 3.14

    # 생성자 메서드
    def __init__(self, radius):
        # 인스턴스 변수
        self.radius = radius

# 객체 생성
c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10

# c1의 인스턴스 변수 pi를 생성
c1.pi = 100

print(c1.pi)  # 100
print(Circle.pi)  # 3.14

# c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi)  # 3.14

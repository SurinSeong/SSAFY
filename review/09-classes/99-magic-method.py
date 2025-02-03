# 매직 메서드

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):  # 내장 함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경한다.
        return f'원의 반지름: {self.radius}'


c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1

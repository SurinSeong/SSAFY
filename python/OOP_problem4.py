# Circle 클래스 : 반지름 정보를 가지고, 원의 면적 계산하는 메서드를 가진다.
# 생성한 객체의 원의 면적을 출력하는 프로그램

class Circle:

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise TypeError ('반지름은 0 초과일 경우만 허용')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * 3.14
    
a = Circle(2)
print(f'원의 면적: {a.area()}')
    
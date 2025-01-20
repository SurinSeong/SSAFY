# Rectangle 클래스
# 가로, 세로 정보를 가지고, 사각형의 면적을 계산하는 메서드를 가짐

class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, width):
        if width < 0:
            raise TypeError('가로 길이는 0 초과를 허용함.')
        self.__width = width

    @height.setter
    def height(self, height):
        if height < 0:
            raise TypeError('세로 길이는 0 초과를 허용함.')
        self.__height = height

    def area(self):
        return self.__width * self.__height

# 생성한 객체의 사각형 면적 출력
a = Rectangle(4, 5)
print(f'사각형의 면적: {a.area()}')
# 부모 클래스 : Shape
# 자식 클래스 : Square -> length 필드
# 0을 반환하는 Shape 클래스의 area 메서드를 length * length 값을 반환하는 메서드로 오버라이딩


class Shape:
    def area(self):
        return 0
    

class Square(Shape):
    
    def __init__(self, length):
        self.__length = length
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length <= 0:
            raise TypeError('길이가 0 초과만 허용함.')
        self.__length = length

    def area(self):
        return self.__length * self.__length
    

square = Square(3)
print(f'정사각형의 면적: {square.area()}')
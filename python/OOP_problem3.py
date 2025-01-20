# 부모 클래스 : Student / name property를 가짐
# 자식 클래스 : GraduateStudent / major property를 가짐

class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.__major = major

    @property
    def major(self):
        return self.__major
    
a = Student('홍길동')
print('이름:', a.name)

b = GraduateStudent('이순신', '컴퓨터')
print(f'이름: {b.name}, 전공: {b.major}')
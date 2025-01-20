# 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체 지향 코드 작성하기
# 학생 클래스의 객체는 객체 생성 시, 국어, 영어, 수학 점수를 저장, 총점을 구하는 메서드 제공

class Student:

    def __init__(self, korean, english, math):
        self.__korean = korean
        self.__english = english
        self.__math = math

    def total_score(self):
        return self.__korean + self.__english + self.__math
    
    @property
    def korean(self):
        return self.__korean
    
    @property
    def english(self):
        return self.__english
    
    @property
    def math(self):
        return self.__math
    
    @korean.setter
    def korean(self, korean):
        if korean < 0:
            raise TypeError('점수는 0 이상의 값만 허용')
        self.__korean = korean

    @english.setter
    def english(self, english):
        if english < 0:
            raise TypeError('점수는 0 이상의 값만 허용')
        self.__english = english

    @math.setter
    def math(self, math):
        if math < 0:
            raise TypeError('점수는 0 이상의 값만 허용')
        self.__math = math

# 객체 생성
a = Student(89, 90, 100)
print(a.total_score())

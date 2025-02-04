# 상속 없는 경우 - 1
class Person:
    # 생성자 메서드
    def __init__(self, name, age):
        # 인스턴스 변수
        self.name = name
        self.age = age

    # 인스턴스 메서드
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

# 인스턴스 생성
s1 = Person('김학생', 23)
p1 = Person('박교수', 59)

s1.talk() # 반갑습니다. 김학생입니다.
p1.talk() # 반갑습니다. 박교수입니다.

# 상속 없는 경우 - 2 : Student, Professor 나눠서 클래스 생성
# 교수 클래스
class Professor:
    # 생성자 메서드
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    # 인스턴스 메서드
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

# 학생 클래스
class Student:
    # 생성자 메서드
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    # 인스턴스 메서드
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

# 상속을 사용한 계층구조 변경
# 사람 클래스 생성 - 상위 클래스
class Person:
    # 생성자 메서드
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 인스턴스 메서드
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

# 교수 클래스 생성 - 하위 클래스
class Professor(Person):
    # 생성자 메서드
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

# 학생 클래스 생성 - 하위 클래스
class Student(Person):
    # 생성자 메서드
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


# 인스턴스 생성
p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk()
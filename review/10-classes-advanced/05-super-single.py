# 단일 상속
# 상위 클래스 생성
class Person:
    # 생성자 메서드
    def __init__(self, name, age, number, email):
        # 인스턴스 변수
        self.name = name
        self.age = age
        self.number = number
        self.email = email

# 하위 클래스 생성
class Student(Person):
    # 생성자 메서드
    def __init__(self, name, age, number, email, student_id):
        # 상위 클래스의 인스턴스 변수
        super().__init__(name, age, number, email)  # super()를 통해 Person의 __init__ 메서드 호출
        # Person.__init__(name, age, number, email)   # 상위 클래스 명을 직접 작성하는 방법
        
        # Student 만의 인스턴스 변수
        self.student_id = student_id


# super를 사용하지 않았을 때 => 생성자 메서드에 인스턴스 변수를 모두 작성해주어야 한다.

# 클래스 메서드

class Person:
    # 클래스 변수
    population = 0
    # 생성자 메서드
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Person.increase_population()
    
    # 클래스 메서드
    @classmethod
    def increase_population(cls):
        cls.population += 1


person1 = Person('Alice')
print(person1.population)
person2 = Person('Bob')
print(person2.population)
print(Person.population)  # 2

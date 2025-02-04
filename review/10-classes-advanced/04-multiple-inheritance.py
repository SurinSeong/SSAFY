# 다중 상속 예시
# 상위 클래스 생성
class Person:
    # 생성자 메서드
    def __init__(self, name):
        self.name = name

    # 인스턴스 메서드
    def greeting(self):
        return f'안녕, {self.name}'
    
# 하위 클래스 생성
class Mom(Person):
    # 클래스 변수
    gene = 'XX'

    # 인스턴스 메서드
    def swim(self):
        return '엄마가 수영'
    
# 하위 클래스 생성
class Dad(Person):
    # 클래스 변수
    gene = 'XY'

    # 인스턴스 메서드
    def walk(self):
        return '아빠가 수영'
    
# 다중 상속
class FirstChild(Dad, Mom):
    # 인스턴스 메서드
    def swim(self):
        return '첫째가 수영'
    
    # 인스턴스 메서드
    def cry(self):
        return '첫째가 응애'
    
# 인스턴스 생성
baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.greeting())
print(baby1.gene)  # XY

print(FirstChild.mro())

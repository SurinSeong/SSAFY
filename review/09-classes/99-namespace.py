class Person:
    # 클래스 변수
    name = 'unknown'

    # 인스턴스 변수
    def talk(self):
        print(self.name)


# 객체 생성
p1 = Person()
p1.talk()  # unknown

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown

# 인스턴스 변수 설정
p2.name = 'Kim'
p2.talk()  # Kim

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim

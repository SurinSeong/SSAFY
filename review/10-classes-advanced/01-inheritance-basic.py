# 상속의 예시

class Animal:
    def eat(self):
        print('먹는 중')


class Dog(Animal): # Dog 클래스는 Animal 클래스를 부모로 가지는 클래스이다.
    def bark(self):
        print('멍멍')


# 인스턴스 생성
my_dog = Dog()

# 인스턴스 메서드 호출
my_dog.bark()

# 부모 클래스 메서드 사용
my_dog.eat()
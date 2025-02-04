# 메서드 오버라이딩 예시
# 상위 클래스 생성
class Animal:
    def eat(self):
        print('먹는 중')

# 하위 클래스 생성
class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print('Dog가 먹는 중')

# 인스턴스 생성
my_dog = Dog()

my_dog.eat()

# 오버로딩 (파이썬 미지원) -> 오버라이딩과는 다른 것
class Example:
    def do_something(self, x):
        print(f'첫 번째 do_something 메서드: {x}')

    def do_something(self, x, y):
        print(f'두 번째 do_something 메서드: {x}, {y}')

example = Example()

example.do_something(10) # TypeError: do_something() missing 1 required positional argument: 'y'
# 파이썬은 함수명이 동일하면 가장 마지막으로 생성한 함수가 진짜 함수라고 생각한다. 즉, 오버로딩 없음.

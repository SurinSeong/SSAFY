print(type('1'))
print(type([1, 2]))

help(str)


## 클래스 파트에서 이어서 할 예정 ##


def add(a, b):
    return a + b


class Calculator:
    def add(self, a, b):
        return a + b
    

# 함수 호출
print(add(1, 2))

# 메서드 호출 -> 객체 호출해서 객체의 무언가를 조작하는 것.
a = Calculator()
print(a.add(1, 2))

########################################
# 메서드 호출 방법

# 문자열 메서드 예시
print('hello'.capitalize())

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
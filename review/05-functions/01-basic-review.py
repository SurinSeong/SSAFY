# 두 수의 합을 구하는 코드
num1 = 9873
num2 = 4839
sum_result = num1 + num2 # 연산자를 사용한 경우
print(sum_result)

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2

# 1. 함수를 호출하여 2. 결과 출력
sum_result = get_sum(num1, num2)
print(sum_result)

# 함수의 구조 확인해보기
def make_sum(pram1, pram2):
    # Docstring
    '''이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    '''
    return pram1 + pram2 # return value


# 함수와 반환 값
# print() 함수는 반환값이 없다.
return_value = print(1)
print(return_value)

def say_hello():
    print('Hello')

print(say_hello())
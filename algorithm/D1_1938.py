# 아주 간단한 계산기
# 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램
# 두 개의 자연수 a, b 는 1부터 9까지의 자연수
# 사칙연산 +, -, *, / 순서대로 연산한 결과 출력
# 나누기 연산의 결과에서 소수점 이하의 숫자를 버린다.

def solution(num1, num2):

    plus = num1 + num2
    minus = num1 - num2
    multi = num1 * num2
    division = int(num1 / num2)

    return plus, minus, multi, division


if __name__ == '__main__':
    a, b = map(int, input().split())

    result1, result2, result3, result4 = solution(a, b)

    print(result1)
    print(result2)
    print(result3)
    print(result4)
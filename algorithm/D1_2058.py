# 자릿수 더하기
# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램
"""
[제약사항]
- 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)

[입력]
- 자연수 N

[출력]
- 각 자릿수의 합
"""


def add_location(number):
    # 자릿수의 합
    total = 0
    # number -> string 처리 후 반복
    for char in str(number):
        # 각 자리를 더하기
        total += int(char)

    return total


if __name__ == '__main__':
    N = int(input())
    total_sum = add_location(N)
    print(total_sum)
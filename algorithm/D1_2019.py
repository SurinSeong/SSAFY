# 1부터 주어진 횟수까지 2를 곱한 값들
# 주어질 숫자를 30을 넘지 않음

def solution(number):
    for n in range(0, number+1):
        print(2**n, end=' ')


if __name__ == '__main__':
    N = int(input())

    solution(N)
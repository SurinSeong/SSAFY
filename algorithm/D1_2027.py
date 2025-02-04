# 대각선 출력하기
def solution(a, b, n):
    for i in range(1, n+1):
        print(b*(i-1), end='')
        print(a, end='')
        print(b*(n-i))


if __name__ == '__main__':
    solution('#', '+', 5)
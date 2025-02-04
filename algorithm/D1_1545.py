# 주어진 숫자부터 0까지 순서대로 찍어보기
def solution(number):
    for n in range(number, -1, -1):
        print(n, end=' ')


if __name__ == '__main__':
    N = int(input())

    solution(N)

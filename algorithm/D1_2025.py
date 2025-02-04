# N줄 덧셈
# 1부터 주어진 숫자만큼 모두 더한 값을 출력

def solution(number):
    total = 0

    for i in range(1, number+1):
        total += i

    return total


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
# 몫과 나머지 출력
# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램
# 각 수는 1이상 10000이하의 정수
# 가장 첫 줄에는 테스트 케이스의 개수 T
# 테스트 케이스의 첫 번째 줄에는 2개의 수

def solution(a, b):
    return a // b, a % b


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        num1, num2 = map(int, input().split())
        result, remain = solution(num1, num2)
        print(f'#{t} {result} {remain}')
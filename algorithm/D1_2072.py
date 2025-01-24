# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력
# 각 수는 0이상 10000 이하의 정수

# 테스트 케이스 개수 입력 받기
T = int(input())

for t in range(1, T+1):

    # 10개의 수 받기
    numbers = list(map(int, input().split()))

    total = sum([number for number in numbers if number % 2 == 1])

    # for number in numbers:
    #     if number % 2 != 0:
    #         total += number

    print(f'#{t} {total}')
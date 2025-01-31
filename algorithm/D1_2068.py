# 10개의 수를 입력받아, 그 중에서 가장 큰 수를 출력하는 프로그램

# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    # 입력받은 숫자를 리스트 안에 담는다.
    numbers = list(map(int, input().split()))
    # max 함수를 사용해 가장 큰 수를 출력한다.
    print(f'#{t} {max(numbers)}')
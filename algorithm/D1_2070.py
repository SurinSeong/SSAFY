# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램

# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    answer = None
    num1, num2 = map(int, input().split())
    # 왼쪽이 크면
    if num1 > num2:
        print(f'#{t} >')
    # 오른쪽이 크면
    elif num1 < num2:
        print(f'#{t} <')
    # 같으면
    else:
        print(f'#{t} =')
        
# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램 작성 (소수점 첫째 자리에서 반올림한 정수 출력)

# 테스트 케이스 개수 입력 받기
T = int(input())

for t in range(1, T+1):

    # 10개 숫자 입력 받기
    numbers = list(map(int, input().split()))
    avg = round(sum(numbers) / len(numbers), 0)

    print(f'#{t} {int(avg)}')
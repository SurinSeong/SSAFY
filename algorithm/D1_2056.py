# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어짐
# 날짜의 유효성 판단 후, 날짜가 유효하면 'YYYY/MM/DD' 형식으로 출력
# 유효하지 않으면 -1 출력
# 월 : 1~12 사이의 값 -> 일 : 1일 ~ 각 달의 마지막 일
# 2월의 경우, 0201~0228 (윤년 고려하지 않음)

def solution(number):
    # 우선 년도는 저장하고 시작
    date_expression = number[:4]

    # 월
    month = number[4:6]
    # 일
    day = number[6:8]

    if (int(month) in [1, 3, 5, 7, 8, 10, 12]) and (1 <= int(day) <= 31):
        date_expression += f'/{month}/{day}'
    elif (int(month) in [4, 6, 9, 11]) and (1 <= int(day) <= 30):
        date_expression += f'/{month}/{day}'
    elif (int(month) == 2) and (1 <= int(day) <= 28):
        date_expression += f'/{month}/{day}'
    else:
        return -1

    return date_expression


if __name__ == '__main__':
    # 테스트 케이스 개수
    T = int(input())
    # 테스트 케이스 반복
    for t in range(1, T+1):
        # 8자리 숫자 받기
        date = input()
        answer = solution(date)
        print(f'#{t} {answer}')
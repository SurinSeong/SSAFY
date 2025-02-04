try:
    # 에러가 날 수 있는 코드 작성
    x = int(input('숫자 입력: '))
    y = 10 / x

except ZeroDivisionError:
    print('0으로 나눌 수 없음.')

except ValueError:
    print('유효한 숫자 아님.')

else:
    print(f'결과: {y}')

finally:
    print('프로그램 종료.')
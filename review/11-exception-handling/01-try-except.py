# try-except
# 에러의 종류에 따라 except 구문 처리를 할 수 있음.
try:
    result = 10 / 0
except ZeroDivisionError: # 0으로 나눌 수 없는 것에 대한 에러
    print('0으로 나눌 수 없습니다.')


try:
    num = int(input('숫자입력 : '))
except ValueError: # 타입에 맞지 않는 값을 넣었을 때 에러
    print('숫자가 아닙니다.')


# 복수 예외처리 1
try:
    num = int(input('100을 나눌 값을 입력하세요: '))
    print(100/num)

except (ValueError, ZeroDivisionError):
    print('제대로 입력해주세요.')

# 복수 예외처리 2
try:
    num = int(input('100을 나눌 값을 입력하시오: '))
    print(100 / num)

except ValueError:
    print('숫자를 넣어주세요.')

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except:
    print('에러 발생!')

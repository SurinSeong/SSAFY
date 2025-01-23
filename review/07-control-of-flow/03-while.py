# while문 예시
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')

# 사용자 입력에 따른 반복

# number = int(input('양의 정수를 입력해주세요.: '))
# while number <= 0:
#     if number < 0:
#         print('음수를 입력했습니다.')
#     else:
#         print('0은 양의 정수가 아닙니다.')
#     number = int(input('양의 정수를 입력해주세요.: '))
# print('잘했습니다!')

while True:
    # 사용자에게 정수 입력 받기
    number = int(input('양의 정수를 입력해주세요.: '))

    if number < 0:
        print('음수를 입력했습니다.')

    elif number == 0:
        print('0은 양의 정수가 아닙니다.')

    else:
        print('잘했습니다!')
        break
# 예외 객체 다루기
my_list = []

try:
    number = my_list[1]

except IndexError as error: # 예외 객체를 받아 상세 정보 활용 가능
    print(f'{error} 발생.')

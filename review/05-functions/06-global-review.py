num = 0  # 전역 변수


def increment():
    global num  # num를 전역 변수로 선언 / num을 전역 변수 하기 전 표현식을 쓰면 안된다.
    num += 1


print(num)  # 0

increment()

print(num)  # 1

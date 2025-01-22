# 입력받을 때 사용하면 가변을 입력받거나, 입력을 풀 때는 함수 인자로 건넬 때만

number = [1, 2, 3]

print(*number) # unpacking : 함수 내부에서만 작동한다.
print(1, 2, 3)

a, b, c = *number # 이렇게는 쓰이지 않음.

a, b, c = number # 다중 할당
print(a, b, c)

[a, b, c] = number
print(a, b, c)
print([a, b, c])

a, b, c = 1, 2, 3
print(a, b, c)
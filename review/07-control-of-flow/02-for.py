# for 문 작동 원리
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

# 문자열 순회
country = 'Korea'

for char in country:
    print(char)

# range 순회

for i in range(5):
    print(i)

# 딕셔너리 순회
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])


# 인덱스로 리스트 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    print(numbers[i])

for i in range(len(numbers)):
    numbers[i] *= 2

print(numbers)  # [8, 12, 20, -16, 10]


# 중첩된 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)

# 중첩 리스트 순회
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)  # ['A', 'B'] ['c', 'd']

for elem in elements:
    for item in elem:
        print(item)  # A B c d

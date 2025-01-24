# ** list.append(x)
# list의 마지막에 x를 추가.
my_list = [1, 2, 3]

my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

print(my_list.append(5))  # append 추가한 코드를 출력해보기. => None

# ** list.extend(m)
# list의 마지막에 Iterable m의 모든 항목을 추가. (+= 과 같은 기능을 한다.)
# 반복 가능한 객체가 아니면 추가 불가함.
my_list = [1, 2, 3]

my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# append와의 비교
my_list = [1, 2, 3]

my_list.append([4, 5, 6])

# my_list.extend(100) # TypeError

# list.insert(index, x)
# list의 index에 x를 삽입.
my_list = [1, 2, 3]

my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]

# list.remove(x)
# list 가장 왼쪽에 있는 (첫 번째) x를 제거. 항목이 존재하지 않을 경우에는 ValueError.
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]

# ** list.pop([index])
# index 값이 없다면, list의 가장 오른쪽에 있는 (마지막) 항목을 "반환" 후 제거.
# index가 있다면 list의 index 항목을 "반환" 후 제거
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(1)

print(item1)  # 5
print(item2)  # 2
print(my_list)  # [1, 3, 4]


# list.clear()
# list의 모든 항목을 삭제한다.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []

# list.index(x)
# list에서 첫 번째로 일치하는 x의 인덱스를 반환.
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1

# list.count(x)
# list에서 x의 개수를 반환.
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3

# ** list.reverse() (!= reversed(seq))
# list의 순서를 역순으로 변경한다.
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse())  # None
print(my_list)  # [9, 1, 8, 2, 3, 1]

# ** list.sort(key=None, reverse=False)
# list를 정렬한다. (매개변수를 이용 가능)
# 기본적으로 오름차순이다. reverse=True는 내림차순으로 정렬한다.
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]

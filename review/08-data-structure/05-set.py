# add
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4) # 요소 추가
print(my_set)

# clear
my_set.clear() # 새 set
print(my_set)

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)

# pop
element = my_set.pop()
print(element)

# discard : 요소가 있으면 지우고 없으면 실행하지 않음
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set)
my_set.discard(10)

# update
my_set.update([1, 4, 5])
print(my_set)

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
print(set1.intersection(set2)) # {1, 3}
print(set1.issubset(set2)) # False
print(set3.issubset(set1)) # True
print(set1.issuperset(set2)) # False
print(set1.union(set2)) # 합집합

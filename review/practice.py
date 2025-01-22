# 혹시 랜덤 시드 넣어주면 메모리 주소도 고정일까?

a = '123'
print(id(a)) # 1659453634224

# a[0] = '4' # TypeError: 'str' object does not support item assignment
a = a.replace('1', '9') # 변경이 아닌 새로 생성한 것이라고 볼 수 있다. (즉, 재할당)
print(a)
print(id(a)) # 1659453609008


print('=== LIST ===')
new_list = [1, 2, 3]
print(new_list, id(new_list)) # 메모리 주소 동일 [1, 2, 3] 2568551175552

new_list[0] = 10
print(new_list, id(new_list)) # [10, 2, 3] 2568551175552

# 값 교환 => 메모리 주소도 교환됨.
x, y = 10, 20
print(x, id(x), y, id(y))

x, y = y, x
print(x, id(x), y, id(y))

print('=== 참조 배열 ===')
a_list = [10, 20, 30, 40]
print(id(a_list), a_list) # 1680223239360
print(id(a_list[0]), a_list[0]) # 1680221235792
print(id(a_list[1]), a_list[1]) # 1680221236112
# 10, 20의 메모리 주소의 차이는 320

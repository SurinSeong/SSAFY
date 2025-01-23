## for-else 문에 대해서

for i in range(10):
    if i == 5:
        print('5번째에서 멈췄습니다.')
        break

# 중간에 for문이 break로 인해서 탈출하지 않고, 끝까지 돌았을 때 실행됨.
else:
    print('전부 돌았습니다.')


## 위의 방식의 원리 ##

flag = False # break 한 적이 있는지 확인하는 boolean 값

for i in range(10):
    if i == 5:
        print('5번째에서 멈췄습니다.')
        flag = True
        break

if not flag:
    print('전부 돌았습니다.')
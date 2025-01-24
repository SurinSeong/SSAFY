## 다중 객체의 복사 ##
## 얕은 복사는 정확히 알고 사용해야 함.

catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]


backup_catalog = list(tuple(catalog))
print(f'백업 ==> {id(backup_catalog)}')
print(f'바꿀 다중 리스트 ==> {id(catalog)}')
print()

# catalog의 내부의 마지막 리스트를 바꾸기 전
## backup_catalog의 내부 리스트의 id 확인해보기 ##
print(f'백업의 0번째 내부 리스트 id 값 : {id(backup_catalog[0])}')
print(f'바꿀 리스트의 0번째 내부 리스트 id 값 : {id(catalog[0])}')
print(backup_catalog[0] == catalog[0]) # True
print(backup_catalog[0] is catalog[0]) # True
'''
==> 내부의 주소는 바뀌지 않는다는 것을 알 수 있음
==> 따라서 내부 리스트의 내용을 바꾼다면 백업과 함께 바뀐다.
==> 복사가 아닌 재할당.
'''

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''

# catalog 내부의 마지막 리스트를 list(tuple())로 바꾸면?
target = list(tuple(catalog[-1]))
print()
print(f'백업의 마지막 내부 리스트 id 값 ==> {id(backup_catalog[-1])}')
print(f'바꿀 리스트의 마지막 내부 리스트 id 값 ==> {id(target)}')
print(target == backup_catalog[-1])
print(target is backup_catalog[-1])
'''
==> 주소가 다르다는 것을 알 수 있음. 복사!
바꿀 리스트를 변경해도 백업이 바뀌지 않음.
'''


# 여기서 변경을 하면?
target[0] = backup_catalog[-1][0][:2]+'을 향한 한 걸음'
target[1] = '내 삶'+ backup_catalog[-1][1][-4:]
target[-1] = f'{backup_catalog[-1][-1][:2]} {backup_catalog[-1][-1][-2:]}의 비밀'

print()
print(f'바꿀 리스트의 마지막 내부 리스트:\n{target}')
print(f'백업의 마지막 내부 리스트:\n{backup_catalog[-1]}')
print(target == backup_catalog[-1])
print(target is backup_catalog[-1])
'''
==> 내용도 다르고 주소도 다르다는 것을 알 수 있다.
복사를 변경한 것이 확실함.
'''

# 다시 catalog의 마지막 리스트에 새로운 변수를 재할당한다.
catalog[-1] = target
print('\n=== 다시 catalog에 넣어주기 ===')
print(f'backup_catalog[-1] 주소 : {id(backup_catalog[-1])}')
print(f'catalog[-1] 주소 : {id(catalog[-1])}')
print(f'change_list 주소 : {id(target)}')


print('\ncatalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
print(catalog == backup_catalog) # 값이 같은지 비교
print(catalog is backup_catalog) # 주소까지 같은지 비교

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)

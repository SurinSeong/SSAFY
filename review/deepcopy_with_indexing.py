catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

backup_catalog = catalog[:]

print(f'backup 주소 : {id(backup_catalog)}')
print(f'catalog 주소 : {id(catalog)}')

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''

print('\n=== 맨 마지막 줄 주소 비교 ===')
print('[다시 슬라이싱 하기 전]')
print(f'backup_catalog[-1] 주소 : {id(backup_catalog[-1])}')
print(f'catalog[-1] 주소 : {id(catalog[-1])}')

# 새로운 변수에 catalog의 마지막 리스트를 슬라이싱을 이용해 할당.
change_list = catalog[-1][:]

print('\n[슬라이싱 후]')
print(f'backup_catalog[-1] 주소 : {id(backup_catalog[-1])}')
print(f'change_list 주소 : {id(change_list)}')

# 새로운 변수인 change_list의 값을 backup_catalog를 이용해 변경
change_list[0] = backup_catalog[-1][0][:2]+'을 향한 한 걸음'
change_list[1] = '내 삶'+backup_catalog[-1][1][-4:]
change_list[-1] = f'{backup_catalog[-1][-1][:2]} {backup_catalog[-1][-1][-2:]}의 비밀'

# 다시 catalog의 마지막 리스트에 새로운 변수를 재할당한다.
catalog[-1] = change_list
print('\n=== 다시 catalog에 넣어주기 ===')
print(f'backup_catalog[-1] 주소 : {id(backup_catalog[-1])}')
print(f'catalog[-1] 주소 : {id(catalog[-1])}')
print(f'change_list 주소 : {id(change_list)}')


print('\ncatalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
print(catalog == backup_catalog) # 값이 같은지 비교
print(catalog is backup_catalog) # 주소까지 같은지 비교

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)

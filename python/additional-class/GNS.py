arr = ['TWO', 'SIX', 'TWO', 'FIV', 'FOR', 'SIX']

print('TWO' < 'FOR') # False
print('TWO' < 'SIX') # False
# 문자열의 대소 비교 실패함.

# 0~9 까지의 단어를 리스트에 저장해서
# 인덱스 확인해서 비교하기

num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
new_list = []

for val in arr:
    for i in range(10):
        if num_list[i] == val:
            new_list.append(i)
            break
        
# 문자열과 대응하는 숫자를 키-값 쌍으로 딕셔너리에 저장해서 활용할 수 있다.
# 카운팅을 통해 글자를 나열할 수 있다. (카운팅 정렬의 원리)

# 빈 딕셔너리에 각 단어가 있는지 확인하고 없으면 만들어주기
# 카운팅 : 자료값을 배열의 인덱스로 사용하는 것이다.
# 1. 인덱스는 양의 정수여야 한다.
# 2. 값을 인덱스로 사용하려면 배열이 이미 만들어져있어야 한다. => 촤댓값을 통해 공간을 미리 만들 수 있음.



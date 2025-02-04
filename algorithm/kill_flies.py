# 2차원 리스트에서 최댓값 찾기
def change_to_flatten_with_idx(matrix):
    flatten_list = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            flatten_list.append((matrix[i][j], (i, j)))

    return flatten_list

# + 모양일 때 파리의 합 구하기
def shape_plus(matrix, middle, length):
    # middle의 좌표 확인
    row, col = middle[1]
    
    range(col-length+1, col+length)



# 테스트 케이스 개수
T = int(input())

for test in range(T):
    # N, M
    N, M = map(int, input().split())

    table = []
    for i in range(N):
        line = list(map(int, input().split()))
        table.append(line)

    flatten = sorted(change_to_flatten_with_idx(table), key=lambda x:x[0], reverse=True)
    print(flatten)
    
    max_box = 2*M - 1

    # +나 x를 사용할 수 있음
    if max_box <= N:
        first_sum = flatten[1]
        for element in flatten:


print(table)
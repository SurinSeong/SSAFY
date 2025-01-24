# 테스트 케이스 개수
T = int(input())

for test in range(T):
    # N, M
    N, M = map(int, input().split())

    table = []
    for i in range(N):
        line = list(map(int, input().split()))
        table.append(line)

    max_box = 2*M - 1
    print(max_box)

    # +나 x를 사용할 수 있음
    if max_box <= N:
        print(max(table))

print(table)
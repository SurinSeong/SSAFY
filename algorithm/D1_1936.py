# 일대일 가위바위보

# 가위 1, 바위 2, 보 3

def solution(num1, num2):
    result = {'A': num1, 'B': num2}

    if result['A'] - result['B'] == 1:
        return 'A'
    elif result['A'] - result['B'] == -1:
        return 'B'
    elif result['A'] - result['B'] == 2:
        return 'B'
    else:
        return 'A'


if __name__ == '__main__':
    A, B = map(int, input().split())

    print(solution(A, B))
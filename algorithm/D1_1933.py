# 간단한 N의 약수
# 입력 : 1개의 정수 N (1 ≤ N ≤ 1,000)
# 정수 N의 약수를 오름차순으로 출력하는 프로그램 작성

def solution(number):
    # 약수 담을 리스트
    new_list = []

    for i in range(1, number+1):
        if number % i == 0:
            new_list.append(i)

    return new_list


if __name__ == '__main__':
    N = int(input())

    result = solution(N)

    for num in result:
        print(num, end=' ')
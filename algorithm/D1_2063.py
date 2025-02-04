# 중간값은 통계 집단의 수치를 크기 순으로 배열했을 때 전체의 중앙에 위치하는 수치
# 입력으로 N개의 점수가 주어졌을 때, 중간값을 출력
"""
- N은 항상 홀수
- N은 9 이상 199 이하의 정수
"""

# 점수의 개수 입력 받기
N = int(input())

# 점수를 리스트 안에 담기
scores = list(map(int, input().split()))

# 점수 오름차순 정렬
scores.sort()

print(scores[len(scores)//2])

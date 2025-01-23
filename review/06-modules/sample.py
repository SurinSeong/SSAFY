# my_math.py를 통해 함수 가져오기
# 경로가 달라지면 경로 설정이 필요하다.
import my_math

print(my_math.add(1, 2))


# 패키지 사용하기
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1, 2))
print(tools.mod(1, 2))

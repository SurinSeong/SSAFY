# 스태틱 메서드 활용
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(3, 5))  # 8

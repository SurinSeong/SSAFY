# 거듭 제곱
def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)


print(power(2, 3))  # 8
print(power(2, 5))  # 32
print(power(2, 10))  # 1024


# 피보나치 수열 
def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test
print(fibonacci(1))  # 1 
print(fibonacci(6))  # 8 
print(fibonacci(10))  # 55

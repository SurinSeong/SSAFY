# .find(x) : x의 첫 번째 위치를 반환. 없으면 -1을 반환.
text = 'banana'
print(text.find('a')) # 'a' 찾아보기
print(text.find('z')) # 'z' 찾아보기

# .index(x) : x의 첫 번째 위치를 반환. 없으면 오류 발생.
print(text.index('a')) # 'a' 찾아보기
# print(text.index('z'))   # 'z' 찾아보기 -> ValueError 발생

# .isupper() : . 앞의 문자열이 모두 대문자로 이루어져 있는지 확인.
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False

# .islower() : . 앞의 문자열이 모두 소문자로 이루어져 있는지 확인.
print(string1.islower())  # False
print(string2.islower())  # False

# .isalpha() : . 앞의 문자열이 알파벳으로만 이루어져 있는지 확인.
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False


## 문자열 조작 메서드 (새 문자열을 반환함.)
# ** str.replace(old, new[, count]) : str에서 old를 new로 바꿔서 반환. count : 바꿀 횟수. (선택적)
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world

# ** str.strip([chars]) : str에서 공백이나 특정 문자를 제거.
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)

# ** str.split(sep=None, maxsplit=-1) : sep를 구분자 문자열로 사용해 str에 있는 단어들의 리스트를 반환.
text = 'Hello, world!'
words1 = text.split(',')
words2 = text.split()
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']


# ** 'separator'.join(iterable) : separator로 iterable의 문자열을 연결한 문자열 반환.
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text)  # Hello-world!

# str.capitalize() : str의 가장 첫 번째 글자를 대문자로 변경.
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# str.title() : str 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환.
new_text2 = text.title()
print(new_text2)  # Hello, World!

# str.upper() : str을 모두 대문자로 변경.
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# str.lower() : str을 모두 소문자로 변경.
new_text4 = text.lower()
print(new_text4)  # hello, world!

# str.swapcase() : str의 대문자는 소문자로, 소문자는 대문자로 변경.
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!
print()

# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())

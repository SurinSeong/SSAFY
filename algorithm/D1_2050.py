# 알파벳을 숫자로 변환

# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력

# 문자열의 최대 길이 : 200
# 알파벳으로 이루어진 문자열
# 각 알파벳을 숫자로 변환한 결과값을 빈칸을 두고 출력

def solution(string):
    for char in string:
        alpha_num = ord(char) - 64
        print(alpha_num, end=' ')


if __name__ == '__main__':
    alpha_string = input()
    solution(alpha_string)

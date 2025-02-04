# 신문 헤드라인
# 신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램
# 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램

def solution(string):
    return string.upper()


if __name__ == '__main__':
    sentence = input()
    print(solution(sentence))
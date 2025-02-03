class Person:
    # 생성자 메서드 : 새로운 객체를 만들 때 필요한 초기값 설정
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')


# 부모 클래스 : Person / getGender 메서드 : 'Unknown' 반환
# 자식 클래스 : Male, Female / 각각 'Male', 'Female' 반환


class Person:
    def getGender(self):
        return 'Unknown'
    

class Male(Person):
    def getGender(self):
        return 'Male'
    

class Female(Person):
    def getGender(self):
        return 'Female'


male = Male()
print(male.getGender())

female = Female()
print(female.getGender())
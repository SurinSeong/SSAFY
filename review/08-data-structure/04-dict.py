# clear
person = {'name' : 'Alice',
          'age' : 25}

person.clear() # 빈 리스트 반환
print(person)

# get
person = {'name':'Alice',
          'age':25}

print(person.get('name'))   # Alice
print(person.get('country'))    # None
print(person.get('country', 'Unknown')) # Unknown
print(person)

# keys
print(person.keys()) # dict_keys(['name', 'age'])

for item in person.keys():
    print(item)

# values
print(person.values()) # dict_values(['Alice', 25])

for item in person.values():
    print(item)

# items
print(person.items())

for key, value in person.items():
    print(key, value)

# pop
print(person.pop('age')) # 25
print(person) # {'name' : 'Alice'}
print(person.pop('country', None)) # None


# setdefault
person = {'name': 'Alice',
          'age': 25}

print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name''Alice','age': 25, 'country':'KOREA'}


# update : 새로운 딕셔너리로 업데이트
person = {'name': 'Alice',
          'age': 25}

other_person = {'name':'Jane', 'country':'KOREA'}
person.update(other_person)
print(person)

person.update(age=100, address='SEOUL')
print(person)


a = {}
b = {'name':'Alice', 'age':25}

a.update(b)
print(a)

b['name'] = 'Bella'
print(a)
print(b)

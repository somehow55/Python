# 함수
a = 2
b = 3
print(a + b)

c = "hi "
d = " there"
print(c + d)

a_list = ['사과', '오렌지', '바나나', '키위']
print(a_list[3])

a_list.append('아보카도')
print(a_list)

a_dict = {
    'firstName': 'sponge',
    'lastName': 'bob'
}
print(a_dict['firstName'])


def sum(x, y):
    print('파이썬 함수')
    return x + y


result = sum(2, 5)
print(result)


# 조건문

def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년입니다')


is_adult(19)
is_adult(49)

# 파이썬에서는, { } 대신에 : 과 들여쓰기로 범위를 지정한다. 들여쓰기 매우 중요!!!


# 반복문1

fruits = ['사과', '바나나', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

count = 0
for aaa in fruits:
    # print(aaa)
    # for문은 여기서부터
    if aaa == '아보카도':
        count += 1
    # 여기까지가 내용물이다

print(count)

# 반복문2
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]


for person in people:
    # print(person)
    if person['age']>20:
        print(person['name'])
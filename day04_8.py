# 튜플 tuple
# tuple = ()
# 튜플 : 추가할 수가 없음

menu = ('돈가스', '순두부', '김밥')         # 추가x
print(menu[0])
print(menu[1])
print(menu[2])

name1 = ''
name2 = ''
name3 = ''

name1, name2, name3 = menu
name1, name2, name3 = ('안녕하세요','Hello','반간습니다')

print(name1, name2, name3)

# 전체 조회
for i in menu:
    print(i)

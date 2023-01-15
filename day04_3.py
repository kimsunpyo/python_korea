cafe_menu = []

# 카페 메뉴 이름 추가
cafe_menu.append('아메리카노')
cafe_menu.append('카페라떼')
cafe_menu.append('아이스티')
cafe_menu.append('유자차')
cafe_menu.append('에스프레소')

print(cafe_menu)

# 데이터의 갯수 len
리스트의갯수 = len(cafe_menu)
print(리스트의갯수)

# 수정
cafe_menu[1] = '띠용'

# 전체 출력
for i in cafe_menu:
    print(i)
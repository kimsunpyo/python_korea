# 기타 제어문
# break, coutinue

# break: 반복문 강제종료
# countinue: 반복문이 안끝났어도 위로 올라감 (1회성 취소, 밑에 있는 코드는 무시)

for i in range(10):
    print((i+1),'번째 Hello')
    if i >= 2:
        break

for i in range(10):
    if i >= 3 and i < 7:
        continue 
    print((i+1),'번째 Bye')
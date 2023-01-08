# 20세 이상은 성인
# 14세 이상은 청소년
# 14세 미만은 어린이
# 0세 미만은?


age = int(input('나이를 입력하세요>>'))
if age>=20:
    print('성인')
elif age>=14:      # 위에 있는 if가 틀렸다는 가정하에 실행
    print('청소년')
elif age>=0:
    print('어린이')
else:
    print('?')

# 2

# 0~7 유치원
# 8~13 초등학교
# 14~16 중학교
# 17~19 고등학교
# 20~23 대학교
# 23~ 회사원
# 0미만은 ?

나이 = int(input('나이는?'))
if 나이 >= 0 and 나이 <=7:
    print('유치원')
elif 나이>=8 and 나이 <=13:
    print('초등학교')
elif 나이 >= 14 and 나이 <=16:
    print('중학교')
elif 나이 >=17 and 나이 <=19:
    print('고등학교')
elif 나이 >=20 and 나이<=23:
    print('대학교')
elif 나이 >=23:
    print('회사원')
else:
    print('사람x')










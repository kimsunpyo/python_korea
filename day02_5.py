# % : 나머지구하기2
# 홀짝 구분 : 2로 나눈 나머지가 1이면 홀수, 0이면 짝수
# 배수: 7의 배수 -> 7로 나눈 나머지가 0이면 7의 배수

# # 자동차 뒷번호가 홀수인지 짝수인지
# 차번호 = int(input("차뒷번호 4자리를 입력하세요>>"))
# if (차번호 % 2) == 0:           # 홀짝을 구분할땐 % 2 활용
#     print('짝수번호 차량')
# else:
#     print('홀수번호 차량')

#     # %연산자를 사용해서 차번호가 5의 배수인지 판별
# carnumber = int(input('차번호가 5의 배수인가요?'))
# if (carnumber%5)== 0:
#     print('5의 배수')
# else:
#     print('5의 배수가 아니다.')

# 숫자 3개를 입력해서 가장 큰 숫자를 찾으시오
# num1 = int(input('정수1 입력>>'))
# num2 = int(input('정수2 입력>>'))
# num3 = int(input('정수3 입력>>'))
# 조건문을 활용해서 가장 큰 숫자를 출력해보세요
# if num1>num2 and num1>num3:
#     print ('가장 큰 수는',num1)
# elif num2>num1 and num2>num3:
#     print ('가장 큰 수는',num2)
# else:
#     print('가장 큰 수는',num3)

# 윤년 판독기 --> 년도를 입력해서 해당하는 년도가 윤년인지 판별
# 윤년 : 해당 년도가 4의 배수이면서 100의 배수가 아닌 년도는 2월이 29일까지
#        있음(단, 예외로 400의 배수면 무조건 윤년)

year = int(input('년도를 입력하세요>>'))
if ((year%4)==0) and ((year%100)!=0):
    print('윤년')
elif year%400==0:
    print('윤년')
else:
    print('윤년x')

# if True:
#     print('if의 조건식 결과가 True면 실행')
# if False:
#     print('if의 조건식 결과가 False면 무시')


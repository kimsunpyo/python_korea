문자열 = 'hello world, my name is python'
정수 = 314
실수 = 3.14

for i in 문자열:
    print(i, end=' ')

i = 0
while i < len(문자열):
    print(문자열[i], end=' ')
    i+=1


# str, int, float, list, tuple, dict, set
# 리스트
# 지하철 3칸, [10,15,12]
subway1 = 10
subway2 = 15
subway3 = 121
print()
# 리스트: 같은 주제의 변수들을 묶음으로 보관 (전체 출력이 가능)
리스트 = [10, 15, 12]
for i in 리스트:
    print(i,'명')


# 문제1 :문자열에서 알파벳 o의 갯수를 알려주세요
문자열 = 'hello world, my name is python'
for i in 문자열:
    print()


#문제2: 1월~12월을 출력하되 입력받은 월은 skip
i=int(input('숫자를 입력하시오'))
for j in range(12):
    print(j+1,'월')
    if j==i:
       break
    
# 문제3: 1월~12월을 출력하되 입력받은 월은 월로부터는 출력안함

# 문제4: 구구단을 만들어주세요 
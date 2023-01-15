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
o_count = 0
for i in 문자열:
    if i == 'o':
        o_count += 1
print(o_count)        


#문제2: 1월~12월을 출력하되 입력받은 월은 skip
skip_month = int(input('건너뛰고자하는 월을 입력하세요>>'))
for i in range(1,13):
    if i == skip_month:
        continue
    print(i,'월')


# 문제3: 1월~12월을 출력하되 입력받은 월은 월로부터는 출력안함
break_month = int(input('몇 월까지 출력할까요?>>'))
for i in range(1,13):
    if i-1 == break_month:
        break
    print(i,'월')


# 문제4: 구구단을 만들어주세요.
for i in range(1,10):
    for j in range(2,10):
        print(j,'x',i,'=',i*j, end='\t')   # \t: 4칸띄어쓰지
    print()

 
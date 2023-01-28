# # return : 함수의 결과를 활용할 수 있게 해준다
# def 절댓값더하기(a,b):
#     if a < 0:
#         a*=-1
#     if b < 0:
#         b*=-1
#     return a+b  # return 옆에 있는 값이 사용한 곳으로 전달

# 결과1 = 절댓값더하기(3,7)       # 10
# 결과2 = 절댓값더하기(-4,결과1)      # 14
# print(결과2)
# print(절댓값더하기(-1,-1))

# 문제1 : 리스트에 저장된 값의 총합을 구하는 함수를 만들고 return값을 활용해  평균을 구해보세요
def 총합(a_lst):
    result = 0      # 함수 안에서 만든 변수는 함수가 끝나면 사라진다(지역변수)
    for i in lst:
        result += i
    # result = a_lst[0] + a_lst[1] + a_lst[2] + a_lst[3] + a_lst[4] 
    return result

lst = [10,20,30,40,50]
sum = 총합(lst)
avg = sum/len(lst)

print('총합은',sum)
print('평균은',avg)

# 문제2 : 입력한 갯수만큼 *을 표시하는 함수
def star(num):
    result = ''
    for i in range(num):
        result += "*"
    return result

# 문자열은 더하면 합쳐짐
s1 = star(int(input('별의개수를 입력하세요>>')))
print(s1)







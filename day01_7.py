# 연산자
a = 10
b = 3

a+b       # 덧셈 13
a-b       # 뺄셈 7 
a*b       # 곱셈 30
a/b       # 나눗셈 3.3
a%b       # 나머지구하기 1
a**b      # a의 b제곱   # 2**3==2*2*2==8

a = b     # b값울 a공간의 대입
a == b    # 같다 (수학의 =)
a != b    # 다르다  
a > b     # a가 크다
a < b     # a가 작다
a >= b    # a가 b보다 크거나 같다 
a <= b    # a가 b보다 작거나 같다  

# 대입연산자 주의할 점 =
a = a     # 왼쪽은 공간의 개념으로 a, 오른쪽은 a안에 들어있는 값

# 줄인말
a += b    # a = a + b
a -= b    # a = a - b
a *= b    # a = a * b
a /= b    # a = a / b

(a + b) * a     #우선순위

# 비교연산자 == , >= >
a=10
b=3
print(a != b)
print(a == b)
print(a > b)

# 관계연산자 and, or ,not
a > 5 and a < 15        # a는 5보다 크고 15보다 작다
print(a > 5 and a < 15 )    # True

a < 0 or a > 5      #a는 0보다 작거나 5보다 크다
print(a<0 or a >5)

# and: 둘다 맞아야만 맞고
# or : 둘 중 하나만 맞아도 맞음
print(a < 0 and a > 5)      # a는 0보다 작지않아서 false
print(a < 0 or a > 100)     #둘다 틀려서 flase 
print(not b==3)             #false는 true로 , true는 false로
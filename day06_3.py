# 파일읽고쓰기

# 파일 만들고 쓰기(txt) : 이미 있으면 쓰기만
def 파일쓰기(filepath):
    f = open(filepath, 'w', encoding='UTF-8') 
    f.write('안녕하세요 반갑습니다 감사합니다\n')      # \n : 엔터키(한줄바꾸기)
    f.close()

# 파일 읽기(txt)
def 파일읽기(filepath):
    f = open(filepath, 'r', encoding='UTF-8')
    # line = f.readline()     # 한줄을 읽어옴
    lines = f.readlines()       # 전체를 읽음
    # print(line)
    print(lines)
    for line in lines:
        print(line, end='')
    f.close()


# 파일 추가쓰기(txt)
def 파일추가쓰기(filepath):
    f = open('sample.txt','a+', encoding='UTF-8')
    f.write('다시 만나요')
    f.close()
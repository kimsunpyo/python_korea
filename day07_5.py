# 자동차 클래스를 만들어보세요
# 속성(멤버변수) : 차주인, 색상, 차종
# 기능(메서드) : 차정보

class 자동차:
    차주인 = ''
    색상 = ''
    차종 = ''
    def __init__(self,차주인,색상,차종):
        self.차주인=차주인
        self.색상=색상
        self.차종=차종
    def 차정보(self):
        print(self.차주인, self.색상, self.차종)
    
    def 차운전(self):
        print(self.차주인,'가 차를 운전합니다')
    

# 클래스 사용예시
아빠차 = 자동차('아빠', 'black', 'gv80')        # 클래스명 옆에 있는 () : __init__ 생성자
엄마차 = 자동차('엄마', 'red', 'g70')
내차 = 자동차('홍길동', 'white', 'k3')

아빠차.차정보()     # 차주인, 차색상, 차종 print
엄마차.차정보()
내차.차정보()


아빠차.차운전()     # 아빠가 차를 운전합니다 print
엄마차.차운전()     # 엄마가 차를 운전합니다 print

# 메서드가 같아도 객체가 다르면 그 객체에 해당하는 메서드와 멤버변수로 사용됨
class Person:
    name=None
    age=0
    def __init__(self,initName="기본이름",initAge=100): #__init__멤버함수는 클래스객체가 생성될때 자동실행됨
        print("클래스 객체가 생성됩니다")
        self.name=initName #객체 생성시 파라미터에 정의된 "기본이름"을 객체.멤버변수에 입력
        self.age=initAge #객체 생성시 파라미터에 정의된 100을 객체.멤버변수에 입력
    def 정보입력(self,pName,pAge):
        self.name=pName #파라미터로 받은 값을 객체.멤버변수에 넣어줌
        self.age=pAge
    def 자기소개(self):
        print("안녕")
        print("나는",self.name,"이야",self.age,"살 이야") #객체.멤버변수를 호출

#테스트
p2 = Person() #클래스를 생성해서 p2객체에 넣음
p2.자기소개() #클래스 객체 p2의 자기소개() 함수를 호출

print(p2.name) #p2의 멤버변수 name 호출
print(p2.age)

p2.정보입력("행복한언덕",23)
p2.자기소개()

print(p2.name)
print(p2.age)

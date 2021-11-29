class Calculator():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def minus(self):
        result = self.first - self.second
        return result	
    def multiple(self):
        result = self.first * self.second
        return result
    def divide(self):
        result = self.first / self.second
        return result
    
class PerfectCal(Calculator):
    pass

#클래스 밖
a=PerfectCal(2,2)
print(a.add())
print(a.minus())
print(a.multiple())

#부모 class의 기능 추가
class PerfectCal(Calculator):
    def modulo(self):
        result = self.first % self.second
        return result

a=PerfectCal(4,2)

print(a.modulo())

#생성자 상속받는 방법 : 자식클래스의 생성자에서 부모 클래스의 생성자 불러오기
class PerfectCal(Calculator):
    def __init__(self,first,second):
        super().__init__(first,second)
        
#부모 클래스의 메소드를 자식클래스에서 다시 정의 : 메소드 오버라이딩
class PerfectCal(Calculator):
    def divide(self):
        result=self.first//self.second
        return result

#부모 클래스 객체
a=Calculator(15,7)
print(a.divide())
#자식 클래스 객체
b=PerfectCal(15,7)
print(b.divide())

#클래스 변수 출력
class Food:
    favorite="뿌링클"

a=Food() #객체를 만들고
b=Food()

print(a.favorite,b.favorite) #객체의 변수 출력
#이걸 클래스 변수라고 함

#클래스 변수 수정:값 바꾸기
Food.favorite="황금올리브"
print(a.favorite,b.favorite)

c=Food()
d=Food()
print(c.favorite,d.favorite)

print(Food.favorite)
print(id(Food.favorite))

#id()함수 : 변수가 공유되는지 여부를 알 수 있음
print(a.favorite)
print(id(a.favorite))
print(b.favorite)
print(id(b.favorite))

#고유값이 같으면 >> 각 변수가 값을 공유하고 있단느 뜻임.
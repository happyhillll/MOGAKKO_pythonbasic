#오늘의 문제 : 계산기 클래스 만들기

class Calculator:
    def setdata(self,first,second):
        self.first=first #a.first=6
        self.second=second #a.second=3
    def add(self):    #add 메소드
        result=self.first+self.second
        return result
    def times(self):
        result=self.first*self.second
        return result
    def devide(self):
        result=self.first/self.second
        return result

'''
    def __int__(self,first,second):
        self.first=first
        self.second=second

a=Calculator()
a.setdata(6,3)
print(a.add())
'''
        
a=Calculator()
a.setdata(6,3)
print(a.add())

b=Calculator()
b.setdata(20.,10)
print(b.first)
print(b.second)
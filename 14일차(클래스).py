class rectangle:
    count=0 #클래스 변수
    
    def __init__(self,width,height): #초기자(initializer)
        #self. : 인스턴스변수
        self.width=width
        self.height=height
        rectangle.count +=1
    
    #메서드
    def calcArea(self):
        area=self.width*self.height
        return area
    #정적메서드
    @staticmethod
    def isSquare(rectWidth,rectHeight):
        return rectWidth == rectHeight

#테스트
square = rectangle.isSquare(5,5)
print(square)
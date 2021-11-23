'''
def 함수명(매개변수1, 매개변수2, ...):
    	함수내용
'''
def getSum(a,b):
    	return a+b
a = 1
b = 2
result = getSum(a,b)
print(result)

#오늘의 문제 : 정수 n까지의 합을 구하는 함수 만들기
#정수 n을 하나 입력받고, 0부터 n까지의 합을 구하는 함수 만들기

a=int(input("정수를 입력하세요. : "))

def moonjae(a):
    sum=0
    for i in range(0,a+1):
        sum=sum+i
    return (sum)
    
result=moonjae(a)
print(result)

#while 문

def moonjae(a):
    sum=0
    while True:
        if a==0:
            return(sum)
            break
        else:
            sum=sum+a #정수 n부터 0까지의 숫자를 더함
            a-= 1 #정수 n을 -1씩 해서 0으로 만듬
print(moonjae(a))
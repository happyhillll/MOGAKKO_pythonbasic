'''
여러분이 가게에 가서 물건을 사려고 해요! 근데 물건의 가격이 3420원이라고 가정해봅시다. 그럼 이때 1000원 지폐, 100원 동전, 10원 동전은 각각 몇 개씩 필요한지 출력해봅시다! 그리고 동전은 몇 개가 필요한지도 출력해봐요!
'''

#몫만 구하기
a = 5.5 / 2    # 실수형의 나눗셈 -> 결과 -> 실수형
b = 5.5 // 2   # 실수형의 버림나눗셈 -> 결과 -> 실수형이지만 소수점 값 버림
c = 5 / 2      # 정수형의 나눗셈 -> 결과 -> 실수형
d = 5 // 2     # 정수형의 버림나눗셈 -> 결과 -> 정수형 (소수점 X)

print(a)
print(b)
print(c)
print(d)

#나머지만 구하기
print(5 % 2)
print(2.5 % 2)

#거듭제곱
print(2 ** 4)   #2의 4승
print(2 ** 10)  #2의 10승

#홀수 판정기
a=7
b=2347
print("a의 나머지는 ",a%2)
print("b의 나머지는 ",b%2)

#오늘의 문제-산술연산자

stuff=3420
a=stuff//1000 #3
b=(stuff-(1000*a))//100 #4
c=(stuff-(1000*a+100*b))//10 #5

print('1000원 : ',a)
print('100원 : ',b)
print('10원 : ',c)
print("필요한 동전의 개수 : ",b+c)
#오늘의 문제 : 짝수이면서 7의 배수는 아닌 수 찾기/입력한 숫자들의 합 구하기
#2) 0이 입력될 때까지 숫자를 계속 입력 받아 입력 받은 숫자들의 합 구하기

sum=0

while True: 
    num=int(input("숫자를 입력하세요. : "))
    if num == 0:
        break
    else:
        sum+=num
print(sum)
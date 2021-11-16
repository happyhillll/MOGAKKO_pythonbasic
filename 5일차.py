#오늘의 문제 - 숫자로 생일을 입력받아 연도와 월, 일을 출력하기
a=int(input("생일을 입력해주세요. : "))
print(type(a))
print(str(a)[0:4]+"년")
print(str(a)[4:6]+"월")
print(str(a)[6:8]+"일")

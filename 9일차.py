#오늘의 문제

year = int(input("연도를 입력하세요 :"))

if  year % 4 != 0:
    print(year,"년은 윤년이 아닙니다.")

elif year % 4 == 0 :
    if year%100 == 0 and year%400 !=0 :
        print(year, "윤년이 아닙니다.")
    else :
        print(year,"년은 윤년입니다.")


print(year%4)

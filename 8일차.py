#오늘의 문제 : bmi 결과보기
'''
키와 몸무게를 입력받아 BMI지수가 25 ~는 '비만입니다.', BMI 지수가 23 ~ 25는 '과체중입니다.', BMI 지수가 18.5 ~ 23는 '정상체중입니다.', BMI 지수가 18.5 미만일 경우에는 '저체중입니다.'를 출력해주는 프로그램을 작성하시오.**
'''
height=int(input("키를 입력하세요. : "))
weight=int(input("몸무게를 입력하세요. : "))
bmi=weight/((height/100)**2)
if bmi>=25:
    print("비만입니다.")
elif 23<=bmi<25:
    print("과체중입니다.")
elif 18.5<=bmi<23:
    print("정상체중입니다.")
else:
    print("저체중입니다.")
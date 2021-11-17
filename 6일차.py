#오늘의 문제 - 조건문
#합격,불합격/ 문장 내 단어 유무 확인 

# 세 과목의 점수를 입력받아 평균 점수가 50점 이상이면 '합격', 50점 미만이면 '불합격'을 출력해주세요.

first=int(input("첫 번째 과목의 점수를 입력하세요. : "))
second=int(input("두 번째 과목의 점수를 입력하세요. : "))
third=int(input("세 번째 과목의 점수를 입력하세요. : "))
avg=(first+second+third)/3

if avg>=50:
    print("평균 점수는 "+str(avg)+"점으로 합격입니다.")
else:
    print("평균 점수는 "+str(avg)+"점으로 불합격입니다.")

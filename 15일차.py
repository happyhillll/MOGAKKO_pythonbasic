#오늘의 문제 : 최댓값의 위치를 구하기
'''
크기(길이)가 6 이상인 리스트를 값과 함께 선언하고 최댓값이 어디에 위치하는지 출력하세요.

[필수조건]

- 매개변수가 있는 함수를 사용하세요.

[참고]

- 입력크기 만큼 반복문을 돌려야겠죠?
- 인덱스를 활용해요!
- 최댓값을 비교할 수 있는 변수가 있다면..?
'''

def whereismax(num):
    temp_max=0
    
    for i in range(1,len(num)):
        if num[i]>num[temp_max]:
            temp_max=i
    return temp_max

temp_list=[12,23,45,64,74.13]
print(whereismax(temp_list))
    
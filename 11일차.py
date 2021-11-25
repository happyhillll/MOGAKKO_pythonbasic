list=[]
a=0

for i in range(7):
    b=int(input("정수를 입력해주세요. : "))
    list.append(b)
    a+=list[i]

print(a/7)
#1)1부터 100까지의 수 중에서 짝수이면서 7의 배수가 아닌 수의 개수를 출력

cnt=0

for i in range(100):
    if i%2==0 and i%7!=0:
        cnt+=1
print(cnt)
#3:28~40
n=int(input())
for i in range(n):
    if i%2==0:
        for j in range(1,n+1):
            print(n*i+j,end=' ')
        print()
    elif i%2==1:
        for j in range(n):
            print(n*(i+1)-j,end=' ')
        print()
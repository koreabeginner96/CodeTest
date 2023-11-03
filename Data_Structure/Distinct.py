#선택 정렬을 사용 해서 풀려고 하였으나 같은 값이 있을 경우 안된다.
a=[2,1,1,2,3,1]
cnt=1
for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j]<a[j-1]:
            temp=a[j]
            a[j]=a[j-1]
            a[j-1]=temp
for i in range(1,len(a)):
    if a[i] != a[i-1]:
        cnt+=1
print(cnt)
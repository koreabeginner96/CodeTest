a=[1,5,3,4,6,8,9,0,21342,15,54,2,6345,63,56,346,34,56]
for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j]<a[j-1]:
            temp=a[j]
            a[j]=a[j-1]
            a[j-1]=temp

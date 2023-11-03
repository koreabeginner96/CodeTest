a=[9,3,9,3,9,7,9]
dict={}
for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j]<a[j-1]:
            temp=a[j]
            a[j]=a[j-1]
            a[j-1]=temp
for x in range(len(a)):
    if a[x] not in dict:
        dict[a[x]]=1
    else:
        dict[a[x]]+=1
for key,values in dict.items():
    if values == 1:
        print(key)

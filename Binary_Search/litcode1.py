#15분40초
def solution(n):
    list=[]
    answer=[]
    cnt=0
    while n>1:
        a=int(n%2)
        list.append(a)
        n/=2
    list.append(n)
    for i in list:
        if i == 1:
            while i!=1:
                cnt+=1
        answer.append(cnt)
    return max(answer)
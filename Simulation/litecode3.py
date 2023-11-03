#2분58초
def solution(X, Y, D):
    Start =X
    End=Y
    jump=D
    cnt=0
    while Start<End:
        cnt+=1
        Start+=jump
    return cnt
from collections import deque
#11분
def rotate(nums: list[int], k: int):
    nums = deque(nums)
    for i in range(k):
        B = nums.pop()
        nums.appendleft(B)
    ans=list(nums)
    return ans
print(rotate(nums = [1,2,3,4,5,6,7], k = 3))
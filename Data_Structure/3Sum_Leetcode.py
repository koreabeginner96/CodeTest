class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        n,m,o=0,1,2
        l=len(nums)
        visited = [False]*l
        while l-2 != n and l!= o:
            if nums[n]+nums[m]+nums[o] == 0:
                if not visited[n] or not visited[m] or not visited[o]:
                    temp=[nums[n],nums[m],nums[o]]
                    visited[n]=True
                    visited[m]=True
                    visited[o]=True
                    ans.append(temp)
            o+=1
            if o==l:
                m+=1
                o=m+1
            if  l-1 == m:
                n+=1
                m=n+1
                o=n+2
        return ans
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        count = 0 
        start = 0
        end = len(nums)-1
        MOD = 10**9 + 7
        nums = sorted(nums)
        while end >= start :
            if nums[start] + nums[end] > target :
                end-=1
            else:
                
                count = (count + pow(2, end - start, MOD)) % MOD
                start+=1   
        return count
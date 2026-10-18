class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if (s%2):
            return False
        target = s//2
        check = [0]*(target+1)
        for i in range(n):
            l = []
            for j in range(len(check)):
                if (check[j]):
                    tot = j + nums[i]
                    if (tot <= target):
                        l.append(tot)
            for j in l:
                check[j] = 1
            if (target >= nums[i]):
                check[nums[i]] = 1
        return True if check[-1] == 1 else False
            
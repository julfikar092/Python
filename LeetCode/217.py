class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


num = [1, 5, 6, 8, 7, 5, 6]
res = Solution()

print(res.containsDuplicate(num))

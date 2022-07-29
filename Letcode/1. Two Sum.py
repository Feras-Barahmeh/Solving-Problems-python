# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        for posX, i in enumerate(nums):
            for j in range(posX + 1, len(nums)):
                if nums[j] == target - i:
                    return sorted([posX, j])

ob = Solution()
print(ob.twoSum([2, 7, 11, 15], 9))

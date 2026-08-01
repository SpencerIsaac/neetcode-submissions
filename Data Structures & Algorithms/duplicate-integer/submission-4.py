class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thisSet = set()
        for num in nums:
            thisSet.add(num)
        return len(thisSet) != len(nums)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_map = {}
        for i in range(len(nums)):
            num = nums[i]
            need = target - nums[i]
            if need in my_map:
                return[my_map[need], i]

            my_map[num] = i
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Given array nums & int Val;  
        # remove all the nums while keeping order the same
        # Then return remaing elements K so the elements are in same order w/ out val

        # inalize k = 0 
        # loop through nums
        # check IF num[i] != val
        #   keep num[k] in place and set it equal to num[i]
        # increment k 

        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

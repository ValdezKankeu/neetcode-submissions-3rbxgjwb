class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Given an Array if nums of size n
        # remove the majority element


        counter = {}
        maxCount, res = 0,0

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
            res = n if counter[n] > maxCount else res
            maxCount = max(counter[n], maxCount)

        return res

        
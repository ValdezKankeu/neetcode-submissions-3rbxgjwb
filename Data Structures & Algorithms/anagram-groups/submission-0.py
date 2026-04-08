class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            count = [0] * 26

            for s in string:
                count[ord(s) - ord('a')] += 1   # ✅ fix 'a'

            key = tuple(count)  # ✅ fix spelling + separate step

            if key not in res:  # ✅ must create list first
                res[key] = []

            res[key].append(string)  # ✅ append string, not s

        return list(res.values())  # ✅ fix return
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            count = [0] * 26

            for s in string:
                count[ord(s) - ord('a')] += 1  

            key = tuple(count)  

            if key not in res: 
                res[key] = []

            res[key].append(string)  

        return list(res.values())  
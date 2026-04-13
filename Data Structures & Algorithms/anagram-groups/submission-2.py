from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)

        for string in strs:
            counter = [0] * 26
            for s in string:
                counter[ord(s)- ord('a')] += 1
            key = tuple(counter)
            anagram_dict[key].append(string)
        return list(anagram_dict.values())
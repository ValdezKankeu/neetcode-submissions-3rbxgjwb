class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Given an array strs 
        # Group all anagrans into sublist
        # return 

        res = defaultdict(list)
        for string in strs: # Get each word in strs
            # map each word
            count = [0] * 26
             # Count will reset to zero each go around
            for s in string:
                # map the word
                count[ord(s)- ord('a')] += 1
            res[tuple(count)].append(string)
        return list(res.values())


        
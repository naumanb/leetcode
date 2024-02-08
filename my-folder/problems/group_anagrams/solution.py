class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        hashmap = defaultdict(list)

        
        for word in strs:
            hashmap[''.join(sorted(word))].append(word)
        
        return hashmap.values()

        
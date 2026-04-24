class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_list = []
        hashmap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]    
            
        my_list = list(hashmap.values())
        return my_list
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_freq_map(s):
            freq_map = [0] * 26
            for i in s:
                freq_map[ord(i) - 97] += 1
            return tuple(freq_map)
        
        anagram_dict = defaultdict(list)
        
        for s in strs:
            anagram_dict[get_freq_map(s)].append(s)
        
        return [v for _,v in anagram_dict.items()]

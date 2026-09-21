class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        first = 0
        last = len(s) - 1

        nums = [0,1,2,3,4,5,6,7,8,9]
        nums = [str(n) for n in nums]
        chars = [chr(i) for i in range(ord('a'), ord('z')+1)]
        alphanumeric = nums + chars

        while first <= last:
            if s[first] not in alphanumeric:
                first += 1
                continue
            if s[last] not in alphanumeric:
                last -= 1
                continue
            if s[first] != s[last]: return False

            first += 1
            last -= 1
        
        return True
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = []
        for s in strs:
            encoding.append(str(len(s)))
            encoding.append('@')
            encoding.append(s)
        encoding = "".join(encoding)
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i <= len(s) - 1:
            str_len = []
            while s[i] != '@':
                str_len.append(str(s[i]))
                i += 1
            str_len = int("".join(str_len))

            i += 1 # skips over the '@'

            string = []
            for j in range(str_len):
                string += s[i]
                i += 1
            
            string = "".join(string)

            strs.append(string)
        return strs

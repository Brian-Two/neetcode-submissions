class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        print("encoded:",res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j+1
            word = s[i: j + 1 + l]
            res.append(word)
            i += l
                
        print("decoded:", res)
        return res


def main():
    print(encode(["Hello","World"]))
    print(decode('5#Hello5#World'))
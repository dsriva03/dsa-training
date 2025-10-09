class Codec():
    def encode(self, str):
        res = ''
        
        for word in str:
            res += str(len(word)) + '#' + word
            
        return res

    def decode(self, str):
        res = []
        i = 0

        while i < len(s):
            j = s.find("#",i)

            word = s[j + 1: len(i: j) + 1]

            res.append(word)

            i = j + 1 + (len(s:j) + 1)
        
        return res

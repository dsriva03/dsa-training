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
            j = s.find("#", i)

            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length
        return res





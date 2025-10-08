class Codec():
    def encode(self, str):
        res = ''
        
        for word in str:
            res += str(len(word)) + '#' + word
            
        return res

    def decode(self, str):





def word_dict_mini(s, wordDict):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            s[i:j]
            if s[i:j] in wordDict:
                print(f"found '{s[i:j]}' in wordDict")
            # else:
            #     print(f"'{s[i:j]}' not in wordDict")
s = "leetcode"
wordDict = {"leet", "code", "lee", "tcode"}

word_dict_mini(s, wordDict)
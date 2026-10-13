class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        str1=""
        str2=""
        for word in word1:
            str1+=word
        for word in word2:
            str2+=word
        return str1==str2
        
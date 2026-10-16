class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result=""
        word=s.split()
        for i in range(k):
            result+=word[i]
            if i < k-1:
                result+=" "
        return result
        
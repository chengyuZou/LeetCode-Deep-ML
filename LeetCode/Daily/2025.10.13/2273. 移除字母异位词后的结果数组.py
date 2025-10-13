# https://leetcode.cn/problems/find-resultant-array-after-removing-anagrams/?envType=daily-question&envId=2025-10-13
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        cnt0 = Counter(words[0])
        for i in range(1 , len(words)):
            word = words[i]
            cnt1 = Counter(word)
            if cnt0 == cnt1:
                continue
            ans.append(word)
            cnt0 = cnt1
        return ans


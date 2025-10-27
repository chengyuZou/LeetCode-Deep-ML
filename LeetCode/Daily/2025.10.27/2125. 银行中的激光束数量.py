class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre_cnt = ans = 0
        for row in bank:
            cnt = row.count('1')
            if cnt > 0:
                ans += pre_cnt * cnt
                pre_cnt = cnt
        return ans

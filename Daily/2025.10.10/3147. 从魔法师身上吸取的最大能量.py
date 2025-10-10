class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = 0
        n = len(energy)
        f = [0] * (n + k)
        for i in range(k , n + k):
            f[i] = energy[i - k] + max(f[i - k] , 0)

        return max(f[-k:])

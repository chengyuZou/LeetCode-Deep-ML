class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        # @cache
        # def dfs(i , energy):
        #     if i < 0:
        #         return 0
        #     if energy == 'A':
        #         return max(dfs(i - 1 , "A") + energyDrinkA[i] , dfs(i - 2 , "B") + energyDrinkA[i])
        #     else:
        #         return max(dfs(i - 1 , "B") + energyDrinkB[i] , dfs(i - 2 , "A") + energyDrinkB[i])
        # return max(dfs(n - 1 , 'A') , dfs(n - 1 , "B"))

        f = [[0 , 0] for _ in range(n + 2)]
        for i , (x , y) in enumerate(zip(energyDrinkA , energyDrinkB)):
            f[i + 2][0] = max(f[i + 1][0] , f[i][1]) + x
            f[i + 2][1] = max(f[i + 1][1] , f[i][0]) + y
        return max(f[-1])

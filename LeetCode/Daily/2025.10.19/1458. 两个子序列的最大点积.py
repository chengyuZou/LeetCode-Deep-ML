class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m , n = len(nums1) , len(nums2)
        @cache
        def dfs(i , j):
            if i < 0 or j < 0:
                return -inf
            return max(dfs(i - 1 , j) , dfs(i , j - 1) , nums1[i] * nums2[j], \
            dfs(i - 1 , j - 1) + nums1[i] * nums2[j])
        return dfs(m - 1 , n - 1)

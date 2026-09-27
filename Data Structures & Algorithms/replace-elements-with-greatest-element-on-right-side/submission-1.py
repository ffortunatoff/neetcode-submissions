class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        ans = [0] * size
        rightMax = -1
        for i in range(size - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans

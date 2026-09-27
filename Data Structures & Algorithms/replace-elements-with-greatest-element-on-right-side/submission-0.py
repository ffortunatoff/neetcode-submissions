class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        for i in range(size):
            arr[i] = -1
            for j in range(i+1, size):
                if arr[j] > arr[i]:
                    arr[i] = arr[j]
        return arr

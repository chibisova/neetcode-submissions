class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            leftover = target - numbers[r]
            if leftover == numbers[l]:
                return [l+1, r+1]
            while numbers[r] + numbers[l] <= target:
                l+=1
                if leftover == numbers[l]:
                    return [min(r+1, l+1),max(r+1, l+1)]
            r -= 1
        return [l+1,r+1]
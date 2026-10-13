class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        nums.sort()

        def dfs(i, current, total):
            if total == target: # save if target is reached
                res.append(current.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target: # since nums is sorted, no later number can work
                    return # stop exploring this branch
                current.append(nums[j]) # choose a number
                dfs(j, current, total + nums[j]) # explore this branch; j allows reusing this number
                current.pop()  # Undo the choice (backtrack)

        dfs(0, [], 0)
        return res
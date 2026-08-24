class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        print ("R id: ", r, " : ", heights[r], " L id: ", l, " : ", heights[l])
        return max_area
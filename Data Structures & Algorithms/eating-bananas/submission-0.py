class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min, k_max = 1, max(piles)
        output = k_max

        while k_min <= k_max:
            k = (k_min + k_max) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p) / k)
            if time <= h:
                output = k
                k_max = k - 1
            else:
                k_min = k + 1
            
        return output
        
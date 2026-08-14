class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums_map = {}
        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1

        output = []
        sorted_map = dict(sorted(nums_map.items(), key=lambda item: item[1]))
        values_tuple = tuple(sorted_map.keys())

        for i in range(-1, -k-1, -1):
            output.append(values_tuple[i])
        return output
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums_map = {}
        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1
        # we have a dictionary of all values
        # for list [1,1,1,2,2,3]
        # {[1:3], [2:2], [3:1]}
        # we need to get k highest reps
        # for k = 2 that would be [1,2]

        output = []
        sorted_map = dict(sorted(nums_map.items(), key=lambda item: item[1]))
        values_tuple = tuple(sorted_map.keys())

        # Problem:
        # if we have repeated values: {[1:2], [2:2]} 
        # it would return duplicate [1,1]

        for i in range(-1, -k-1, -1):
            output.append(values_tuple[i])
        return output
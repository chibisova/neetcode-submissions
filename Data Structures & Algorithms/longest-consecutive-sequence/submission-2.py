class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = {}
        num_set = set(nums)
        longest_seq = 0

        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                current_seq = 1

                while cur_num + 1 in num_set:
                    current_seq += 1
                    cur_num += 1
                
                longest_seq = max(current_seq, longest_seq)
        return longest_seq
                
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def populate(num_arr, res_arr, curr_arr, curr_idx):
          curr_arr.sort()
          if curr_arr not in res_arr:
            res_arr.append(curr_arr)

          if curr_idx == len(num_arr):
            return

          populate(num_arr, res_arr, curr_arr + [num_arr[curr_idx]], curr_idx+1)
          populate(num_arr, res_arr, curr_arr, curr_idx+1)


        result = [[]]
        populate(nums, result, [], 0)
        return result

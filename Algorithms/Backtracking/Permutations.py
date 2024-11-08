class Solution:
    def permute(self, nums):
        result = []
        self.bt(nums, [], result)
        return result

    def bt(self, nums, temp_list, result):
        if len(temp_list) == len(nums):
            result.append(list(temp_list))
        else:
            for num in nums:
                if num in temp_list:
                    continue
                temp_list.append(num)
                self.backtrack(nums, temp_list, result)
                temp_list.pop()

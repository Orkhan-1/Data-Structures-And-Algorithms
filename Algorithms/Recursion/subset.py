class Subset:

    def recursion(self, nums, target_sum, temp_sum=0, index=0):
        if target_sum == temp_sum:
            return True

        if temp_sum > target_sum or index >= len(nums):
            return False

        include = self.recursion(nums, target_sum, temp_sum + nums[index], index + 1)
        exclude = self.recursion(nums, target_sum, temp_sum, index + 1)

        return include or exclude

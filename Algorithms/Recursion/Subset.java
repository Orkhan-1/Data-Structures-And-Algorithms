public class Subset {

    private boolean recursion(int[] nums, int targetSum, int tempSum, int index) {
        if (targetSum == tempSum) {
            return true;
        }

        if (tempSum > targetSum || index >= nums.length) {
            return false;
        }

        boolean include = bt(nums, targetSum, tempSum + nums[index], index + 1);
        boolean exclude = bt(nums, targetSum, tempSum, index + 1);

        return include || exclude;
    }

}

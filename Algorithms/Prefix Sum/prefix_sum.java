public class PrefixSum {

    private static int[] prefixSum = null;

    public static void calculatePrefixSum(int[] arr) {
        prefixSum = new int[arr.length + 1];
        for (int k = 1; k <= arr.length; k++) {
            prefixSum[k] = prefixSum[k - 1] + arr[k - 1];
        }
    }

    public static int sumRange(int[] arr, int i, int j) {
        if (prefixSum == null) {
            calculatePrefixSum(arr);
        }
        return prefixSum[j + 1] - prefixSum[i];
    }
}

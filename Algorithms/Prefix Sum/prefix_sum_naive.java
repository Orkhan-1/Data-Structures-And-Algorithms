public class SumRange {
    public static int sumRange(int[] arr, int i, int j) {
        int total = 0;
        for (int index = i; index <= j; index++) {
            total += arr[index];
        }
        return total;
    }
}

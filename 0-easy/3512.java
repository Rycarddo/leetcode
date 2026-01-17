class Solution {
    public int minOperations(int[] nums, int k) {
        int counter = 0;

        int sum = 0;

        for (int num : nums) {
            sum += num;
        };

        while (sum % k != 0) {
            sum--;
            counter++;
        };
        
        return counter;

    }
}
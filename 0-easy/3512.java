class Solution {
    public int minOperations(int[] nums, int k) {
        int big = nums[0];
        int idx = 0;
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > big) {
                big = nums[i];
                idx = i;
            };
        };

        int sum = 0;

        for (int num : nums) {
            sum += num;
        };

        while (sum % k != 0) {
            nums[idx]--;
            counter++;
            sum = 0;

            for (int num : nums) {
            sum += num;
            };

        };
        
        return counter;

    }
}
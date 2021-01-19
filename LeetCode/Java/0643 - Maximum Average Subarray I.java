/*
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/
*/

class Solution {
    public double findMaxAverage(int[] nums, int k) {

        double max = Double.NEGATIVE_INFINITY, avg = 0, sum = 0;

        for (int j = 0; j < nums.length; j++) {
            sum += nums[j];

            if (j >= k - 1) {
                avg = sum / k;
                max = Math.max(avg, max);
                sum -= nums[j + 1 - k];
            }

        }
        return max;
    }
}
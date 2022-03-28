/*
704. Binary Search
https://leetcode.com/problems/binary-search/
*/
class Solution {
    public int search(int[] nums, int target) {
        
        return bin_search(nums, target, 0, nums.length-1);
        
    }
    
    public int bin_search(int[] nums, int target, int low, int high){
        if (low > high){
            return -1;
        }
        
        int mid = low + (high - low) / 2;
        
        if (nums[mid] == target){
            return mid;
        }
        
        if (nums[mid] < target){
             return bin_search(nums, target, mid+1, high);
        }
        if (nums[mid] > target){
             return bin_search(nums, target,low, mid-1);
        }
        return -1;
    }
}
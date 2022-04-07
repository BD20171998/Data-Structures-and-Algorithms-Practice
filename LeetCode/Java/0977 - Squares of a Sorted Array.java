/*
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
*/
class Solution {
    public int[] sortedSquares(int[] nums) {

        int i =0;
        int j=1;
        int temp;
        
        for (i=0; i<nums.length; i++){
            nums[i]=nums[i]*nums[i];
        }
        
        i =0;
         j=1;
        
        while (i<nums.length-1){
             
            while (j<nums.length && nums[j]<=nums[i]){
                temp = nums[i];
                nums[i]=nums[j];
                nums[j]= temp;
                ++j;
            }
  
            ++i;
            j=i+1;
                    }
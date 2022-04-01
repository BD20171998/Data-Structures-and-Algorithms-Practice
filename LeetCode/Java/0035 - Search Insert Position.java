/*
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
*/

class Solution {
    
    public int binary_search(int [] nums,int low,int high,int target){
          
          if (low>high){
              return high+1;
          }
           
          int mid = low + (high-low)/2 ;
          
          if (nums[mid]==target){
              return mid;
          } 
          
          if (nums[mid] > target){
              return binary_search(nums,low, mid-1,target);
          }
          if (nums[mid] < target){
              return binary_search(nums,mid+1,high,target);
          }  
          if (nums[mid-1]<target && nums[mid]>target){
              return mid;
          }
     return -2;
}
  
  public int searchInsert(int[] nums, int target) {
      
      return binary_search(nums, 0,nums.length-1,target);
  }
  

}
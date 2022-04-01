/*
278. First Bad Version
https://leetcode.com/problems/first-bad-version/
*/

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

      public class Solution extends VersionControl {
        public int firstBadVersion(int n) {
                   
            return search(1,n);
        }
        
        public int search(int left,int right)
       
        {
                if (left > right){
                    return -1;
                }
                
                int mid = left + (right-left) / 2;
                
                if (isBadVersion(mid-1) == false && isBadVersion(mid) == true){
                  
                    return mid;}
    
        
                if (isBadVersion(mid) == false){
                    System.out.println("im here now");
                    
                    return search(mid+1,right);
                }
        
                if (isBadVersion(mid) == true){
                    return search(left,mid-1);
                }
                return -2;
        }
    }
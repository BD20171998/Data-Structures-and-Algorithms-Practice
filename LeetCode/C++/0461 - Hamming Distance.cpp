/*
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/
*/

class Solution {
public:
    int hammingDistance(int x, int y) {
    
    int binaryNum1[32] = {}; 
    int binaryNum2[32] = {}; 
    
    int i = 0, hamming = 0; 
        
    while (x > 0) { 
  
        binaryNum1[i] = x % 2; 
        x = x / 2; 
        i++; 
    } 
  
    i = 0;
        
    while (y > 0) { 
  
        binaryNum2[i] = y % 2; 
        y = y / 2; 
        i++; 
    } 
        
    for (int j = 31; j >= 0; j--) 
        if (binaryNum1[j] != binaryNum2[j])
            hamming+=1;
        
    return hamming;
    }
    
};
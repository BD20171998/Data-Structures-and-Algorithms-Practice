/*
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
*/

/**
 * @param {number} numRows
 * @return {number[][]}
 */
 var generate = function(numRows) {
    
    let pascal_triangle = [[1]];
  
    if(numRows===1)
        return pascal_triangle;
    
    else{
        
        for (let i = 1; i < numRows; i++) {
            
            let temp = [1];
          
            for(let j=0; j<i-1;j++)
                {
                 let sum = pascal_triangle[i-1][j]+ pascal_triangle[i-1][j+1];
                    temp.push(sum);
                }
            temp.push(1);
            pascal_triangle.push(temp);
        }
        return pascal_triangle;
    }
    
};
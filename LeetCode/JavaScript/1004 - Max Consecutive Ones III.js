/**
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
*/

/**
 * @param {number[]} A
 * @param {number} K
 * @return {number}
 */
var longestOnes = function(A, K) {
    var k_count = 0;
    var counter = 0;
    var max_ones = 0;
    var WinEnd = 0;

    for (let WinStart = 0; WinStart < A.length; WinStart++) {
        if (A[WinStart] === 0) k_count += 1;

        if (k_count < K + 1) {
            counter = WinStart - WinEnd + 1;
            max_ones = Math.max(counter, max_ones);
        }

        if (k_count === K + 1) {
            while (A[WinEnd] === 1) WinEnd += 1;

            WinEnd += 1;
            k_count -= 1;
        }
    }
    return max_ones;
};
/**
1502. Can Make Arithmetic Progression From Sequence
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
*/

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canMakeArithmeticProgression = function (arr) {
  
    arr.sort(function (a, b) {
    return a - b;
  });
  var diff = Math.abs(arr[1] - arr[0]);

  for (let i = 1; i < arr.length; i++)
    if (Math.abs(arr[i] - arr[i - 1]) !== diff) return false;

  return true;
};

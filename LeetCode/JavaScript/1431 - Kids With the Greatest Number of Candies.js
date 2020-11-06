/**
1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
*/

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
  var max = candies[0];
  var maxIndex = 0;
  var ans = [];

  for (var i = 0; i < candies.length; i++) {
    if (candies[i] > max) {
      maxIndex = i;
      max = candies[i];
    }
  }
  for (var i = 0; i < candies.length; i++) {
    if (candies[i] + extraCandies >= max) ans.push(true);
    else ans.push(false);
  }
  return ans;
};

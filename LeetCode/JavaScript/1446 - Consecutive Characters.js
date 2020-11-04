/**
1446. Consecutive Characters
https://leetcode.com/problems/consecutive-characters/
*/

/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function (s) {
  var cur_max = 1,
    power = 1;

  for (let i = 1; i < s.length; i++) {
    if (s[i] === s[i - 1]) cur_max += 1;
    else cur_max = 1;

    power = Math.max(power, cur_max);
  }
  return power;
};

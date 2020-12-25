/*
66. Plus One
https://leetcode.com/problems/plus-one/
*/

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    var ans = [];
    var carry = 0;

    digits[digits.length - 1] += 1;

    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] + carry > 9) {
            ans.unshift(0);
            carry = 1;
        } else if (carry + digits[i] < 10) {
            ans.unshift(digits[i] + carry);
            carry = 0;
        }
    }

    if (carry === 1) ans.unshift(1);

    return ans;
};
/**
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
*/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {

    var vowels = ['a', 'e', 'i', 'o', 'u'];
    var count = 0;
    var temp = 0;
    var i = 0;
    while (i <= s.length - 1)

    {
        if (vowels.includes(s[i]))
            temp += 1;

        if (i >= k && vowels.includes(s[i - k]))
            temp--;

        count = Math.max(temp, count);

        i += 1;
    }

    return count;
};
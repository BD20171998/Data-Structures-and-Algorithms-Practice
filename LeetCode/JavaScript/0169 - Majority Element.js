/*
169. Majority Element
https://leetcode.com/problems/majority-element/
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let counts = {};
    let max = 0;
    let index = 0;

    for (let i = 0; i < nums.length; i++) {
        if (!(nums[i] in counts)) counts[nums[i]] = 1;
        else counts[nums[i]] += 1;
    }

    const keys = Object.keys(counts);

    for (const key of keys) {
        if (counts[key] >= max) {
            max = counts[key];
            index = key;
        }
    }
    return index;
};
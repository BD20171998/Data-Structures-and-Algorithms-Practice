/**
824. Goat Latin
https://leetcode.com/problems/goat-latin/
*/

/**
 * @param {string} S
 * @return {string}
 */
var toGoatLatin = function (S) {
  var count = 1;
  var vowels = ["a", "e", "i", "o", "u"];
  var str = S.split(" ");
  var new_S = "";

  for (let i = 0; i < str.length; i++) {
    if (vowels.includes(str[i][0].toLowerCase())) new_S += str[i];
    else new_S += str[i].slice(1) + str[i][0];

    new_S += "ma" + "a".repeat(count) + " ";

    count += 1;
  }

  return new_S.slice(0, -1);
};

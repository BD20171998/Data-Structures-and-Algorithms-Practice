/*
804. Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words/
*/

/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {

    let morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    let transforms = {};
    let morse_dict = {};

    var a = 97;
    for (var i = 0; i < 26; i++)
        transforms[String.fromCharCode(a + i)] = morse[i];


    for (var j = 0; j < words.length; j++) {
        var temp = ""
        for (var i = 0; i < words[j].length; i++) {
            temp += transforms[words[j][i]];
        }
        if (morse_dict.hasOwnProperty(temp))
            morse_dict[temp] += 1;

        else
            morse_dict[temp] = 1;
    }

    return Object.keys(morse_dict).length;

};
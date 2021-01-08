/**
1232. Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/
*/

/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {


    var m = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0]);
    var b = coordinates[0][1] - (m * coordinates[0][0]);
    var c = 0;

    if (!isFinite(m)) {

        for (let i = 1; i < coordinates.length; i++)
            if (coordinates[i][0] !== coordinates[i - 1][0])
                return false;

        return true;
    } else {
        for (let i = 1; i < coordinates.length; i++) {
            c = coordinates[i][1] - (m * coordinates[i][0]);

            if (c !== b)
                return false;
        }
        return true;
    }
};
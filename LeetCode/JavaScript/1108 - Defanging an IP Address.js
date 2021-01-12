/**
1108. Defanging an IP Address
https://leetcode.com/problems/defanging-an-ip-address/
*/

/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {

    var defanged = "";

    for (let i = 0; i < address.length; i++) {
        if (address[i] === '.')
            defanged += "[.]";

        else
            defanged += address[i];
    }
    return defanged;
};
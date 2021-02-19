/**
415. Add Strings
https://leetcode.com/problems/add-strings/
*/

#include <string>
class Solution
{
public:
    string addStrings(string num1, string num2)
    {

        int carry = 0,
            i = num1.size() - 1,
            j = num2.size() - 1,
            x,
            y,
            s = 0;

        vector<char> sum;

        while (i >= 0 || j >= 0)
        {
            x = (i < 0) ? 0 : num1[i--] - '0';
            y = (j < 0) ? 0 : num2[j--] - '0';

            s = carry + x + y;
            carry = s / 10;

            sum.insert(sum.begin(), '0' + s % 10);
        }

        if (carry > 0)
            sum.insert(sum.begin(), '0' + carry);

        string ans(sum.begin(), sum.end());

        return ans;
    }
};
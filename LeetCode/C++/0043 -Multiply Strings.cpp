/**
43. Multiply Strings
https://leetcode.com/problems/multiply-strings/
*/

#include <string>
class Solution
{
public:
    string multiply(string num1, string num2)
    {

        if (num1[0] == '0' || num2[0] == '0')
            return "0";

        vector<int> product(num1.size() + num2.size(), 0);
        int temp;

        for (int i = num1.size() - 1; i >= 0; i--)
        {
            for (int j = num2.size() - 1; j >= 0; j--)
            {
                temp = (num1[i] - '0') * (num2[j] - '0') + product[i + j + 1];

                product[i + j + 1] = temp % 10;

                product[i + j] += temp / 10;
            }
        }

        if (product[0] == 0)
            product.erase(product.begin());

        stringstream result;
        copy(product.begin(), product.end(), ostream_iterator<int>(result));

        string s = result.str();
        return s;
    }
};
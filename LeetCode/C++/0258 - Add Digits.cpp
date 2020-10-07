/*
258. Add Digits
https://leetcode.com/problems/add-digits/
*/

class Solution
{
public:
    int sum(int x)
    {
        int temp_sum = 0;

        while (x != 0)
        {
            temp_sum += x % 10;
            x /= 10;
        }
        return temp_sum;
    }

    int addDigits(int num)
    {
        int temp = 10, y = num;

        while (temp > 9)
        {

            temp = sum(y);
            y = temp;
        }

        return temp;
    }
};
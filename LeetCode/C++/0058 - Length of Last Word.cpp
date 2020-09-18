//58. Length of Last Word
//https://leetcode.com/problems/length-of-last-word/

#include <string>
class Solution
{
public:
    int lengthOfLastWord(string s)
    {

        if (s.length() == 0 || (s.length() == 1 && s[0] == 32))
            return (0);

        if (s.length() == 1 && s[0] != 32)
            return (1);

        int length = 0;

        for (int i = s.length() - 1; i >= 0; --i)
        {

            if (s[i] != 32)
            {
                length += 1;

                if (i - 1 < 0 || s[i - 1] == 32)
                    break;
            }

            else if (s[i] == 32)
                continue;
        }
        return (length);
    }
};
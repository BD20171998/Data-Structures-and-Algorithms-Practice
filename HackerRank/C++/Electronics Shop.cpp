/*
Electronics Shop
https://www.hackerrank.com/challenges/electronics-shop/problem
*/

int getMoneySpent(vector<int> keyboards, vector<int> drives, int b) {
   
    int cur_max=-1,sum;

    for (long unsigned int i=0;i<keyboards.size();i++)
    {
        if (keyboards[i] > b)
            continue;

        for (long unsigned int j=0;j<drives.size();j++)
        {
            sum = keyboards[i]+drives[j];
            if (sum > cur_max && sum<=b)
                cur_max=sum;

            else if (sum > b)
                continue;
        }
    }
    return cur_max;
}
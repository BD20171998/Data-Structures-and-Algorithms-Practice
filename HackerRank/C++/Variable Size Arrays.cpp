/*
Variable Sized Arrays
https://www.hackerrank.com/challenges/variable-sized-arrays/problem
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{

    int i, j, length, n, q, temp;

    cin >> n;
    cin >> q;

    vector<int> v[n];

    for (int k = 0; k < n; k++)
    {
        cin >> length;
        for (int l = 0; l < length; l++)
        {
            cin >> temp;
            v[k].push_back(temp);
        }
    }

    for (int m = 0; m < q; m++)
    {
        cin >> i;
        cin >> j;
        cout << v[i][j] << "\n";
    }

    return 0;
}
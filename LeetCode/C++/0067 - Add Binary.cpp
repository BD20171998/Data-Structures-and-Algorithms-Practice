/**
67. Add Binary
https://leetcode.com/problems/add-binary/
*/

class Solution {
public:
    string addBinary(string a, string b) {
        
       if (a.size()==1 && b.size()==1)
        {
            if ((a[0]-'0') + (b[0]-'0') == 0)
                return "0";
            
            else if ((a[0]-'0') + (b[0]-'0') == 1)
                return "1";
        }
       
        int l1=a.size()-1, l2=b.size()-1, n1,n2,size;
        vector<char> v; 
        int carry=0,i=0, sum;
        
        while (l1>=0 || l2>=0 || carry ==1)
        {
            n1= l1>=0 ? a[l1]-'0':0;
            n2= l2>=0 ? b[l2]-'0':0;
            sum = n1+n2+carry;
            
            if (sum==0)
            {
                v.insert(v.begin(), '0');
                carry = 0;
            }
            
            else if (sum==1)
            {
                v.insert(v.begin(), '1');
                carry =0;
            }

            else if (sum==2)
            {
                v.insert(v.begin(), '0');
                carry = 1;
            }
               
            else if (sum==3)
            {
                v.insert(v.begin(), '1');
                carry = 1;
            }
            
            l1--;
            l2--;
        }

        string s(v.begin(), v.end());
        
        if (v[0]=='0')
            s.erase(s[0]);
      
        return s;
    }
};
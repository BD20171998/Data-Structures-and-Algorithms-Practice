/**
1457. Pseudo-Palindromic Paths in a Binary Tree

*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        
        // unordered_map<int, int> counts;
        	
        int counts [10] = { };
        return backtrack(root, counts);
        
    }
    
    int backtrack(TreeNode* root,int *counts)
    {
        
        if (root == NULL)
            return 0;
        
        int odd, result=0;
        counts[root->val]+=1;
        
        if (root->left ==NULL && root->right==NULL)
        {
            odd = 0;
            
            for (int i=0; i<10;i++)
            {
                if (counts[i] %2 !=0)
                    odd++;
            }
            
            if (odd<=1)
                result++;
        }
   
        else
        {
            
            result = backtrack(root->left,counts)
            + backtrack(root->right,counts);
            
        }
        
        counts[root->val]-=1;
        return result;
    }
};
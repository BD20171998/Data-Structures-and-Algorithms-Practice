/**
 * 98. Validate Binary Search Tree
 * https://leetcode.com/problems/validate-binary-search-tree/
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} root
 * @return {boolean}
 */

var isValidBST = function (root, mx = null, mn = null) {
  if (root == null) return null;
  if (mx != null && root.val >= mx) return false;
  if (mn != null && root.val <= mn) return false;

  if (root.left != null && isValidBST(root.left, root.val, mn) === false)
    return false;
  if (root.right != null && isValidBST(root.right, mx, root.val) === false)
    return false;

  return true;
};

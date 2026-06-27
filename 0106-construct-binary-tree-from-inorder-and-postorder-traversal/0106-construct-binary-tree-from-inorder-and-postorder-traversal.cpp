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
TreeNode* Tree(vector<int>&inorder, vector<int>&postorder, int in_start, int in_end, 
                int post_start, int post_end,unordered_map<int,int>&map){
        if(in_start > in_end || post_start > post_end) return NULL;

        int rootVal = postorder[post_end];
        TreeNode* root = new TreeNode(rootVal);
        int in_root_idx = map[rootVal];
        int leftSubTreeSize = in_root_idx - in_start;
        root->left = Tree(inorder, postorder, in_start, in_root_idx-1, post_start, post_start+leftSubTreeSize-1, map);
        root->right = Tree(inorder, postorder, in_root_idx+1, in_end, post_start+leftSubTreeSize, post_end-1, map);
        return root;
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map<int,int>map;
        for(int i=0;i<inorder.size();i++){
            map[inorder[i]] = i;
        }
        return Tree(inorder, postorder, 0, inorder.size()-1, 0, postorder.size()-1, map);
    }
};
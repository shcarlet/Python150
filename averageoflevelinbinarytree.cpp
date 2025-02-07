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
    vector<double> averageOfLevels(TreeNode* root) {
       
        vector<double>res;
        queue<TreeNode*>q1;
        q1.push(root);
        while(!q1.empty())
        {
            vector<int>level;
            int qlen=q1.size();
            for(int i=0;i<qlen;i++)
            {
                TreeNode*node=q1.front();
                q1.pop();
                level.push_back(node->val);
                if(node->left)
                {
                    q1.push(node->left);

                }
                if(node->right)
                {
                    q1.push(node->right);
                }
            }
            double sum=0;
            for(int i=0;i<level.size();i++)
            {
                sum=sum+level[i];
            }
            double mean=sum/level.size();
            res.push_back(mean);
        }

        return res;
    }
};

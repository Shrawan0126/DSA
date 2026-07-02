class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int total_sum = 0;
        for(int i : nums) total_sum += i;

        vector<int>res;
        int temp = 0;
        for(int i=nums.size()-1; i>=0; i--){    // 10 9 8 4 3
            temp += nums[i];
            res.push_back(nums[i]);
            if(temp > total_sum - temp) break;
        }

        return res;
    }
};
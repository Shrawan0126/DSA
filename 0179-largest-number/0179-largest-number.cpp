class Solution {
public:
    static bool cmp(string &a, string &b){   //compare a = 3, b = 30
        return a + b > b + a;               // 330 < 303
    }
    string largestNumber(vector<int>& nums) {
        vector<string>temp;
        for(int n : nums) temp.push_back(to_string(n));
        sort(temp.begin(), temp.end(), cmp);

        if(temp[0] == "0") return "0";

        string res = "";

        for(int i=0; i<temp.size(); i++){
            res = res + temp[i];
        }

        return res;
    }
};
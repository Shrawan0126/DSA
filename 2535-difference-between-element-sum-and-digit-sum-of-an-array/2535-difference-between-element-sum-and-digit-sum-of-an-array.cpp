class Solution {
public:
    void Digit_sum(int n, int &d_sum){
        while(n){
            d_sum += n%10;
            n /= 10;
        }
    }
    int differenceOfSum(vector<int>& nums) {
        int sum = 0, d_sum = 0;
        for(int i : nums){
            sum += i;
            Digit_sum(i,d_sum);
        }

        return abs(sum - d_sum);
    }
};
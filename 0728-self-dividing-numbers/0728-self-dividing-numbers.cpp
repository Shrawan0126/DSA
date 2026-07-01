class Solution {
public:
    bool isDivisible(int num){
        int rem,n=num;
        while(num){
            rem = num%10;
            if(rem == 0 || n % rem != 0) return false;
            num /= 10;
        }
        return true;
    }
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int>res;

        for(int i=left; i<=right; i++){
            if(isDivisible(i)) res.push_back(i);
        }

        return res;
    }
};
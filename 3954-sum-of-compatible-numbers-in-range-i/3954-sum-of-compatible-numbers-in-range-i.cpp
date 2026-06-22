class Solution {
public:
    int sumOfGoodIntegers(int n, int k) {
        int res = 0;

        for(int x=1; x<=n+k; x++){
            if(abs(n-x) > k) continue;
            if( (n&x) == 0){
                res += x;
            }
        }

        return res;
    }
};
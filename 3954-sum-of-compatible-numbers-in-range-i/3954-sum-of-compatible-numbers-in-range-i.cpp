class Solution {
public:
    int find(int x,int n,int k,int &res){
        if(x > n+k) return 0;
        if(abs(n-x) > k) return find(x+1,n,k,res);

        if( (n&x) == 0){
            res += x;
        }

        return find(x+1,n,k,res);
    }
    int sumOfGoodIntegers(int n, int k) {
        int res = 0;
        find(1,n,k,res);
        return res;
    }
};
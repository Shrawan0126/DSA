class Solution {
public:
    string makeSmallestPalindrome(string s) {
        int i=0,j=s.size()-1;
        while(i<j){
            if(s[i] != s[j]){
                char x = min(s[i],s[j]);
                s[i] = s[j] = x;
            }
            i++;
            j--;
        }
        return s;
    }
};
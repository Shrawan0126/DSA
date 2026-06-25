class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        int l=0, r = s.size()-1;

        while(l<r){
            while(l<r && vowels.find(s[l]) == vowels.end()) l+=1;
            while(l<r && vowels.find(s[r]) == vowels.end()) r-=1;

            swap(s[l],s[r]);
            l+=1;
            r-=1;
        }

        return s;
    }
};
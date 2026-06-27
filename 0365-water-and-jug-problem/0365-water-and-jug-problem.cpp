class Solution {
public:
    bool DFS(int a,int b,int x,int y,int target, set<pair<int,int>>&visited){
        if(a == target || b == target || a + b == target) return true;

        if(visited.count({a,b})) return false;
        visited.insert({a,b});


        if(DFS(x, b , x, y, target, visited)) return true;
        if(DFS(a, y , x, y, target, visited)) return true;

        if(DFS(0, b , x, y, target, visited)) return true;
        if(DFS(a, 0 , x, y, target, visited)) return true;

        int t = min(a,y-b);
        if(DFS(a-t, b+t , x, y, target, visited)) return true;
        t = min(x-a, b);
        if(DFS(a+t, b-t , x, y, target, visited)) return true;
        
        return false;
    }
    bool canMeasureWater(int x, int y, int target){
        set<pair<int,int>>visited;
        return DFS(0, 0, x, y, target, visited);
    }
};
// Runtime
// 124ms
// Beats 85.62% of users with C++

// Memory
// 105.42MB
// Beats 25.93% of users with C++

// used help from jk_Kdcgc on this solution
#include <stack>

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> indices;
        int n = temperatures.size();
        vector<int> ans(n);

        indices.push(0);
    
        for (int i = 1; i < n; i++){
    
            while (!indices.empty() && temperatures[indices.top()] < temperatures[i]){
                ans[indices.top()] = i - indices.top();
                indices.pop();
            }
            indices.push(i);
        }
        for (int i = 0; i < indices.size(); i++){
            ans[indices.top()] = 0;
            indices.pop();
        }

        return ans;
    }
};

// Runtime
// 16ms
// Beats 95.41% of users with C++

// Memory
// 11.73MB
// Beats 31.20% of users with C++

class Solution {
public:
    int firstUniqChar(string s) {
        int n = s.size();
        vector<int> v(26,0);
        for (int i = 0; i < n; i++){
            v[s[i]-'a']++;
        }
        for (int i = 0; i < n; i++){
            if (v[s[i]-'a'] == 1){
                return i;
            }
        }
        return -1;
    }
};

// Runtime
// 3ms
// Beats 26.41% of users with C++

// Memory
// 7.50MB
// Beats 19.56% of users with C++

#include <bitset>

class Solution {
public:
    bool isPowerOfTwo(int n) {

        std::string s = std::bitset< 64 >( n ).to_string(); // string conversion
        
        int count = 0;
        for (int i = 0; i < s.size(); i++){
            if (s[i] == '1') count++;
            if (count == 2) return false;
        }
        if (count == 1) return true;
        return false;
    }
};

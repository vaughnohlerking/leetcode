// Runtime
// 3ms
// Beats 17.15% of users with C++

// Memory
// 7.52MB
// Beats 8.37% of users with C++

#include <string>

class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> v;
 
        string options = "123456789";
        vector<int> combinations;

        for (int i = 2; i <= 9; i++){
            for (int j = 0; j <= 9-i; j++){
                combinations.push_back(stoi(options.substr(j,i)));
            }
        }
        for (int i = 0; i < combinations.size(); i++){
            if (combinations[i] >= low && combinations[i] <= high){
                v.push_back(combinations[i]);
            }
        }
        
        return v;
    }
};

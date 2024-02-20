// Runtime
// 21ms
// Beats 20.76% of users with C++

// Memory
// 20.30MB
// Beats 47.57% of users with C++

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size() + 1;
        long int summ = (n * (n-1))/2;
        n--;
        long int total = 0;
        for (int i = 0; i < n; i++){
            total += nums[i];
        }
        return summ - total;
    }
};

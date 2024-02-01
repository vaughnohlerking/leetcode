// Runtime
// 144ms
// Beats 90.20% of users with C++

// Memory
// 110.53MB
// Beats 95.42% of users with C++

class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
  
        sort(nums.begin(), nums.end());
        vector<vector<int>> emptyArr(0, vector<int> (3, 0)) ;
  
        int arrs = nums.size() / 3;
        vector<vector<int>> v(arrs, vector<int> (3, 0)) ;

        int ith;
        for (int i = 0; i < arrs; i++){
            ith = 3*i;
            if (nums[ith + 2] - nums[ith] <= k){
                v[i][0] = nums[ith];
                v[i][1] = nums[ith + 1];
                v[i][2] = nums[ith + 2];
            }else return emptyArr;
        }
        return v;
    }
};

// Runtime 15ms
// Beats 50.17%

// Memory 15.62MB
// Beats 7.47%

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> umap; 
        if (nums.size() < 3) {
            return {0,1};
        }
        for (int i = 0; i < nums.size(); i++){
            umap[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++){
            if (umap.count(target - nums[i]) == 1 && umap[target-nums[i]] != i){

                return {i,umap[target-nums[i]]};
            }
        }
        return {};
    }
};

// Runtime
// 55ms
// Beats 17.64% of users with C++

// Memory
// 31.32MB
// Beats 6.77% of users with C++

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>,vector<int>> profiles;
        
        for (int i = 0; i < strs.size(); i++){
            vector<int> profile (26,0);
            for (int j = 0; j < strs[i].size(); j++){ // build string profile
                profile[strs[i][j]-'a']++;
            }
            if  (profiles.count(profile) == 0) profiles[profile]= {i};// add it to grouping
            else profiles[profile].push_back(i);

        }
        vector<vector<string>> v;
        map<vector<int>, vector<int>>::iterator it = profiles.begin(); 
        
        while (it != profiles.end()){ // take mapped values and put them in returned vector
            vector<string> stArr;
            vector<int> indices;
            indices = it->second;
            for (int i = 0; i < indices.size(); i++){
                stArr.push_back(strs[indices[i]]);
            }
            v.push_back(stArr);
            it++;
        }
        return v;
    }
};

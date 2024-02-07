// Runtime 10ms
// Beats 68.64% of users with C++

// Memory 10.88MB
// Beats 24.38% of users with C++

class Solution {
public:
    string frequencySort(string s) {
        
        vector<int> count(75,0);
        map<int,string> m;
    
        for (long int i = 0; i < s.size(); i++){ 
            count[s[i]-'0']++;
        }

        for (int i = 0; i < 75; i++){
            cout << count[i] << " ";
        }
        cout << endl;
        for (int i = 0; i < 75; i++){
            if (count[i] > 0){
                if (m[count[i]] == ""){
                    m[count[i]] = i + '0';
                }
                else{
                    m[count[i]] += i + '0';
                }
            }
            
        }
        sort(count.begin(),count.end());
        string output = "";
        for (int i = 74; i >= 0; i--){

            if (count[i] == 0) break;
            if (i < 74 && count[i] == count[i+1]) continue;

            for (int j = 0; j < m[count[i]].size(); j++){
                for (int k = 0; k < count[i]; k++){
                    output += m[count[i]][j];
                }
            }
            
        }

        return output;
    }
};

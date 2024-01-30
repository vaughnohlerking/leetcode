// Runtime
// 0ms
// Beats 100.00% of users with C++

// Memory
// 15.42MB
// Beats 10.51% of users with C++

#include <cstring>
#include <iostream>
#include <stack>

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack;
        int n = tokens.size();
        if (n == 1){
            return stoi(tokens[0]);
        }
        int l, r, total = 0;

        for (int i = 0; i < n; i++){
            if (isSign(tokens[i])){
                r = stack.top();
                stack.pop();
                l = stack.top();
                stack.pop();
                stack.push(eval(l,r,tokens[i]));
            }
            else stack.push(stoi(tokens[i]));
        }

        return stack.top();
    }

    bool isSign(string s) {
        if (s == "+" || s == "-" || s == "*" || s == "/") return true;
        else return false;
    }

    int eval(int left, int right, string operand) {
        if (operand == "+") return left + right;
        else if (operand == "-") return left - right;
        else if (operand == "*") return left * right;
        else if (operand == "/") return left / right;
        else return 0;
    }
};

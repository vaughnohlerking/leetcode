// Runtime
// 4ms
// Beats 8.52% of users with C++

// Memory
// 8.35MB
// Beats 12.38% of users with C++

# include <stack>
# include <iostream>

class MyQueue {

private:
    stack <int> in;
    stack <int> out;
public:
    MyQueue() {
    }
    void push(int x) {
        in.push(x);
    }
    
    int pop() {
        int val = peek();
        out.pop();
        return val;
    }
    
    int peek() {
        if (out.size() == 0){
            while (in.size() > 0){
                out.push(in.top());
                in.pop();
            }
        }
        return out.top();
    }
    
    bool empty() {
        return in.size() == 0 && out.size() == 0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */

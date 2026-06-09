class Solution {
  public:
    bool isBalanced(string& s) {
        stack<char> st;

        for (char ch : s) {
            // If opening bracket, push
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            }
            else {
                // If closing bracket and stack is empty
                if (st.empty()) return false;

                char top = st.top();
                st.pop();

                // Check matching
                if (
                    (ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '[')
                ) {
                    return false;
                }
            }
        }

        // If stack is empty, all brackets matched
        return st.empty();
        
    }
};




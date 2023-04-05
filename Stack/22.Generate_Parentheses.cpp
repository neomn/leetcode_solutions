class Solution {
public:
    vector<string> result;
    string cur;
    void helper(int open, int close, int n) {
        if (cur.size() == n*2) {
            result.emplace_back(cur);
            return;
        }
        if (open < n) {
            cur.push_back('(');
            helper(open+1, close, n);
            cur.pop_back();
        }
        if (close < open) {

        }
    }
};

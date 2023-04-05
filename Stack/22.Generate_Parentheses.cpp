class Solution {
public:
    vector<string> result;
    string cur;
    void helper(int open, int close, int n) {
        if (cur.size() == n*2) {
            result.emplace_back(cur);
        }
    }
};

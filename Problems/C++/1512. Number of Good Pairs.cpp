class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int res = 0;
        unordered_map<int, int> count;
        for (int n: nums) {
            res += count[n]++;
        }
        return res;
    }
};
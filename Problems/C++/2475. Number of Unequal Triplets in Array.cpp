class Solution {
public:
    int unequalTriplets(vector<int>& nums) {
        int count = 0, prev = 0, nxt = nums.size();
        unordered_map<int, int> frequency;

        for (int n : nums) 
            frequency[n]++;
        
        for (auto[n, freq] : frequency)
        {
            nxt -= freq;
            count += prev * freq * nxt;
            prev += freq;
        }
        return count;
    }
};
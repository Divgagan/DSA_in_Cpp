class Solution {
private:
    void solve(int index, int n, vector<int> &nums, int sum,
               vector<vector<int>> &dp, vector<bool> &possible) {

        // BASE CASE
        if (index == n) {
            possible[sum] = true;
            return;
        }

        // DP HIT
        if (dp[index][sum] == 1) return;

        dp[index][sum] = 1;

        // EXCLUDE
        solve(index + 1, n, nums, sum, dp, possible);

        // INCLUDE
        solve(index + 1, n, nums, sum + nums[index], dp, possible);
    }

public:
    vector<int> DistinctSum(vector<int> nums) {
        int n = nums.size();

        int max_sum = 0;
        for (int x : nums) max_sum += x;

        vector<vector<int>> dp(n + 1, vector<int>(max_sum + 1, 0));
        vector<bool> possible(max_sum + 1, false);

        solve(0, n, nums, 0, dp, possible);

        vector<int> ans;
        for (int s = 0; s <= max_sum; s++) {
            if (possible[s]) ans.push_back(s);
        }

        return ans;
    }
};

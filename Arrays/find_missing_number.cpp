class Solution {
public:
    int missingNum(vector<int>& arr) {
        long long n = arr.size();
        long long N = n + 1;

        long long sum = N * (N + 1) / 2;

        long long total_sum = 0;
        for (const auto &it : arr) {
            total_sum += it;
        }

        return (int)(sum - total_sum);
    }
}; 


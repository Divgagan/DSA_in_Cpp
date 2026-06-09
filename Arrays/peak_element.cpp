class Solution {
  public:
    int peakElement(vector<int> &arr) {
        int n = arr.size();

        // single element
        if (n == 1) return 0;

        // check first element
        if (arr[0] >= arr[1]) return 0;

        // check middle elements
        for (int i = 1; i < n - 1; i++) {
            if (arr[i] >= arr[i - 1] && arr[i] >= arr[i + 1]) {
                return i;
            }
        }

        // check last element
        return n - 1;
    }
};

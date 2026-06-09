class Solution {
public:
    int getSecondLargest(vector<int> &arr) {
        if (arr.size() < 2) return -1;

        int largest = -1;
        int second = -1;

        for (auto x : arr) {
            if (x > largest) {
                second = largest;
                largest = x;
            }
            else if (x < largest && x > second) {
                second = x;
            }
        }

        return second;
    }
};

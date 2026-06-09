class Solution {
public:
    vector<int> findTwoElement(vector<int>& arr) {

        int repeating = -1;
        int missing = -1;

        for (int i = 0; i < arr.size(); i++) {

            int index = abs(arr[i]) - 1;

            if (arr[index] < 0) {
                repeating = abs(arr[i]);   // FIX HERE
            } else {
                arr[index] = -arr[index];
            }
        }

        for (int j = 0; j < arr.size(); j++) {
            if (arr[j] > 0) {
                missing = j + 1;
                break;
            }
        }

        return {repeating, missing};
    }
};

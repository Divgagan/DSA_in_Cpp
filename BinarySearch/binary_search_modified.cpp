class Solution {
public:
    int binarysearch(vector<int> &arr, int k) {

        // Goal:
        // Agar k multiple times present ho,
        // to uska FIRST (smallest index) return karna hai

        int low = 0, high = arr.size() - 1;

        // ans stores the best (smallest) index found so far
        // agar k na mile to -1 return hoga
        int ans = -1;

        while (low <= high) {

            // mid calculation (overflow safe)
            int mid = low + (high - low) / 2;

            if (arr[mid] == k) {
                // k mil gaya → possible answer store karo
                ans = mid;

                // FIRST occurrence chahiye,
                // isliye left side me aur search karte hain
                high = mid - 1;
            }
            else if (arr[mid] < k) {
                // k right side me hoga
                low = mid + 1;
            }
            else {
                // k left side me hoga
                high = mid - 1;
            }
        }

        // loop ke baad:
        // ans = first occurrence index
        // ya -1 (agar k present nahi hai)
        return ans;
    }
};

class Solution {
  public:
    int findFloor(vector<int>& arr, int x) {
        int low = 0, high = arr.size() - 1;
        int ans = -1;

        while(low <= high) {
            int mid = low + (high - low) /2      ;

            if(arr[mid] <= x) {
                ans = mid;      
                low = mid + 1;  
            }
            else {
                high = mid - 1;
            }
        }

        return ans;
    }
};

// In this mine approach is like : 
// First i made two pointer low and high and then i will find the mid element and check if it is less than or equal to x then i will update the ans and move the low pointer to mid + 1 else i will move the high pointer to mid - 1 and at the end i will return the ans which is the index of the floor element.
// Time Complexity: O(log n) where n is the size of the array.
// Space Complexity: O(1) as we are using constant space.
// This is the optimal approach as we are using binary search to find the floor element in logarithmic time.

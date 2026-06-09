class Solution {
  public:
    int minPlatform(vector<int>& arr, vector<int>& dep) {
        
        int N = arr.size() ;  
        sort(arr.begin() , arr.end()) ; 
        sort(dep.begin() , dep.end()) ;
        
        int count = 0 ; 
        int max_count = 0 ; 
        int i = 0 ; 
        int j = 0 ;
        while (i < N ){
            
            if (arr[i] <= dep[j]){
                i++ ; 
                count =count+1   ; 
                
            }
            else {
                count = count-1  ; 
                j++ ; 
            }
            
            max_count = max(max_count , count ) ; 
        }
        return max_count ; 
        
    }

};
// Here in this i have used two pointer approach to solve this problem 
// First i have sorted both the arrival and departure time array
// Then i have used two pointer approach to traverse both the arrays
// If the arrival time is less than or equal to departure time then we need a platform so we increment the count and move the arrival pointer
// Else we can free a platform so we decrement the count and move the departure pointer
// Finally we keep track of the maximum count of platforms needed at any time and return that as the result
// Time Complexity : O(NlogN)
// Space Complexity : O(1)


class Solution {
  public:
    int findEquilibrium(vector<int> &arr) {
        // code here
        
        int total_sum = 0  ; 
        for (int x : arr) {
            total_sum +=x ; 
            
        }
        
        int left_sum = 0 ; 
        
        for (int i = 0 ; i < arr.size() ; i ++ ) {
            int right_sum = total_sum - left_sum - arr[i] ; 
            
            if (right_sum == left_sum ) {
                return i ; 
            }
            
            left_sum +=arr[i] ; 
        }
        
        return -1 ; 
        
    }
};
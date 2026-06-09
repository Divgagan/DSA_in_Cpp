class Solution {
private: 
int solve(int index , vector<int> & arr , int sum  , vector<vector<int>> & dp ){
    // base case ;
    if (index == 0){
        if (sum == 0 && arr[0] == 0) return 2;
        if (sum == 0 || arr[0] == sum) return 1;
        return 0;
    }
    
    if (dp[index][sum] != -1 ){
        return dp[index][sum] ; 
    }
    
    int not_take = solve(index-1 , arr , sum , dp  ) ; 
    
    int take = 0 ; 
    
    if(arr[index] <= sum  ){
        take = solve(index -1 , arr , sum-arr[index] , dp ) ; 
    }
    
    return dp[index][sum] = take + not_take ; 
}
  public:
    int perfectSum(vector<int>& arr, int target) {
        
        int n = arr.size() ; 
        vector<vector<int>> dp (n , vector<int> (target+1  , -1 )) ; 
        
        return solve(n-1 , arr, target , dp ) ; 
        
        
        
    }
};
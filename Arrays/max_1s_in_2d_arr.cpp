class Solution {
  public:
    int rowWithMax1s(vector<vector<int>> &arr) {
        
        int n = arr.size();          
        if(n == 0) return -1;
        
        int m = arr[0].size();       
        
        int row = 0;
        int col = m - 1;             
        int ans = -1;
        
        while(row < n && col >= 0){
            
            if(arr[row][col] == 1){
                ans = row;          
                col--;               
            }
            else{
                row++;               
            }
        }
        
        return ans;
    }
};
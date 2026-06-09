class Solution {
  public:
    int maxProduct(vector<int>& arr) {

        int pref = 1 ; 
        int sufix = 1 ; 
        int n = arr.size() ; 
        int ans = INT_MIN ; 
        
        for(int i = 0   ;i < n ; i++ ){
            if(pref == 0 ) pref = 1 ; 
            if(sufix == 0 ) sufix = 1 ; 
            
            pref = pref * arr[i] ; 
            sufix = sufix * arr[n- i -1 ] ; 
            
            ans  = max (ans , max(pref , sufix )) ; 
            
            
        }
        return ans ; 
        
        
    }
};
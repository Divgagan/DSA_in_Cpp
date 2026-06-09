class Solution {
  public:
    int kthSmallest(vector<int> &arr, int k) {
        priority_queue<int> pq ; 
        
        for(int num : arr) {
            pq.push(num ) ;
            if (pq.size() > k ) {
                pq.pop() ; 
            }
            
            
        }
        
        return pq.top() ; 
        
       
        
        
    }
};

// Time Complexity: O(N log K)
// Space Complexity: O(K)
// I have used the max heap of size k to store the k smallest elements
        // The answer will be at the top of the max heap
        
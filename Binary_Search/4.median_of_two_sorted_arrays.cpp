#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {

public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int count1 = nums1.size(), count2 = nums2.size();
        int totalCount = count1 + count2, half = totalCount >> 1;
        
        // set nums1 to be the smaller array
        if (count1 > count2){
            nums1.swap(nums2);
            count1 ^= count2;
            count2 ^= count1;
            count1 ^= count2;
         }
        

          
    }
};

int main(){
  Solution* s = new Solution();
  vector<int> v1 = {1, 2};
  vector<int> v2 = {3, 4};
  double result = s->findMedianSortedArrays(v1, v2);
  cout << result << endl;
  return 0;
}

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
        
        int l = 0, r = count1-1, mid, j;
        while (true){
            mid = (l+r) >> 1;
            j = half - mid - 2; 

            int n1Left = mid >= 0 ? nums1[mid] : INT_MIN;
            int n1Right = mid+1 < count1 ? nums1[mid+1] : INT_MAX;
            int n2Left = j >= 0 ? nums2[j] : INT_MIN;
            int n2Right = j+1 < count2 ? nums2[j+1] : INT_MAX;

            if (n1Left <= n2Right && n2Left <= n1Right){
               if (totalCount % 2 != 0)
                  return min(n1Right, n2Right);
               return (max(n1Left, n2Left) + min(n1Right, n2Right)) / 2.0;
            }
            else if (n1Left > n2Right)
               r = mid - 1;
            else 
               l = mid + 1;
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

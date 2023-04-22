#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {

public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {        

          
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

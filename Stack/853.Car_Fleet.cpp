#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int carFleet(int target, const std::vector<int>& position, const std::vector<int>& speed) {
    vector<pair<int,int>> car;
    int n = speed.size();
    for(int i=0; i<n; i++)
        car.emplace_back({position[i], speed[i]});
    sort(sort.begin(),car.end());
    stack<float> stk;

}

int main() {
    cout << carFleet(12, {10,8,0,5,3}, {2,4,1,1,3}) << endl;
    return 0;
}



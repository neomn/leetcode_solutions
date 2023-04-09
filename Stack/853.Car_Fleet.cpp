#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int carFleet(int target, const std::vector<int>& position, const std::vector<int>& speed) {
    vector<pair<int,int>> car;
    int n = speed.size();
    for(int i=0; i<n; i++)
        car.emplace_back(position[i], speed[i]);
    sort(car.begin(),car.end());
    stack<float> stk;
    for(int i = n - 1; i >= 0 ; i--) {
        float timeToArrive = (float) (target - car[i].first) / (float)car[i].second;
        if(!stk.empty() && timeToArrive <= stk.top())
            continue;
    }
}

int main() {
    cout << carFleet(12, {10,8,0,5,3}, {2,4,1,1,3}) << endl;
    return 0;
}



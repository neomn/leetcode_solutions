
class TimeMap {
public:     
    unordered_map<string, vector<pair<int, string>>> store;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        store[key].push_back({timestamp, value}); 
    }
    
    string get(string key, int timestamp) {
      if (store.find(key) == store.end()) 
         return "";
      
      auto& vec = store[key];
      int n = vec.size();
      if (timestamp >= vec[n-1].first) 
         return vec[n-1].second;
         
      
    }
};

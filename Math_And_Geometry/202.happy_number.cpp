    
bool isHappy(int n) {
  unordered_set<int> sums;
  int sum = 0;
  int digit;
  while (true) {
    sum = 0;
    while (n >= 1) {
      digit = n % 10;
      sum += digit * digit;
      n /= 10;
    }
  }
}

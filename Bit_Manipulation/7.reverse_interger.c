int reverse(int x){
    int MAX=2147483647, MIN=2147483648, res=0, digit=0;
    while(x != 0){
        digit = x % 10;
        x = x / 10;
        if  ((res > MAX/10 || (res == MAX && digit > MAX%10)) || 
             (res < MIN/10 || (res == MIN && digit < MIN%10)))
                return 0;
        res = (res * 10) + digit;
    }
    return res;
}

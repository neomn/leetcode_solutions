func reverse(x int) int {
    MAX, MIN, res, digit := 2147483647, -2147483648, 0, 0
    for x != 0 {
        digit = x % 10
        x /= 10
        if  (res > MAX/10 || (res == MAX && digit > MAX%10)) || 
            (res < MIN/10 || (res == MIN && digit < MIN%10)){
                return 0
            }
        res = (res * 10 ) + digit
    }
    return res
}

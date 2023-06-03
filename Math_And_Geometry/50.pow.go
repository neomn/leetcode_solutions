func myPow(x float64, n int) float64 {
    res := helper(x, abs(n))
    if n>=0 {return res} else {return 1/res}
}

func helper(x float64, n int) float64 {
    if n==0 {return 1}
    if x==0 {return 0}
    temp := helper(x*x, n/2)
    if n%2 != 0 {return temp*x} else {return temp}
}

func abs(n int) int {
    if n < 0 {return -n}
    return n
}

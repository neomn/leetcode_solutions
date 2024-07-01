func threeConsecutiveOdds(arr []int) bool {
    tsum := 0
    for _,n := range(arr) {
        if n % 2 == 0 {tsum = 0} else {tsum++}
        if tsum == 3 {return true}
    }
    return false
}

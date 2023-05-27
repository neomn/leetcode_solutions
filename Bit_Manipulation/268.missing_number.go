func missingNumber(nums []int) int {
    n := len(nums)
    sum, sum2 := (n*(n+1))/2, 0
    for _, num := range nums{
        sum2 += num
    }
    return sum-sum2
}

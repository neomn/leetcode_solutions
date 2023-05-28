
func getSum(a int, b int) int {
    var carry int
    for b != 0 {
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    }
    return a
}

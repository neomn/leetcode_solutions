func largestOddNumber(num string) string {
    for i:=len(num)-1; i>-1; i-- {
        if int(num[i]) % 2 != 0{
            return num[:i+1]
        }
    }
    return ""
}

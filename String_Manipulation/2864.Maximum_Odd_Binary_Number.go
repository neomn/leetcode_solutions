func maximumOddBinaryNumber(s string) string {
    c := strings.Count(s, "1")
    return strings.Repeat("1",c-1) + strings.Repeat("0",len(s)-c) + "1" 
}

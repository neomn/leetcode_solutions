func findCenter(edges [][]int) int {
    var e1,e2,e3,e4 = edges[0][0], edges[0][1], edges[1][0], edges[1][1]
    if e1 == e3 || e1 == e4 { return e1 }
    return e2
}

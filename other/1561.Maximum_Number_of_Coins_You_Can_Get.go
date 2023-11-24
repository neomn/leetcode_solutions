package main

import "sort"

func maxCoins(piles []int) int {
	idx := len(piles) - 2
	var res, counter = 0, len(piles) / 3
	sort.Ints(piles)
	for i := 0; i < counter; i++ {
		res += piles[idx]
		idx -= 2
	}
	return res
}

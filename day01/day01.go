/* ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## */

// Day 01

// -----------------------------------

package main

// Imports
import (
	// Input/Output
	"fmt"
	"os"

	// String manipulation
	"strings"
	// Other required import
	"slices"
)

// -----------------------------------
// Functions //

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func countOcc(slice []int, target int) int {
	count := 0
	for _, value := range slice {
		if value == target {
			count++
		}
	}
	return count
}

func part_one(col_a []int, col_b []int) int {
	var part1 int = 0

	//fmt.Println(col_a)
	//fmt.Println(col_b)

	for i, a := range col_a {
		diff := a - col_b[i]

		part1 += max(diff, -diff)
	}

	return part1
}

func part_two(col_a []int, col_b []int) int {
	var part2 int = 0

	set_a := make([]int, len(col_a))
	copy(set_a, col_a)

	slices.Compact(set_a)

	for _, num := range set_a {
		cnt_a := countOcc(col_a, num)
		cnt_b := countOcc(col_b, num)

		val := cnt_a * cnt_b * num

		part2 += val
	}

	return part2
}

func main() {
	fmt.Println("Day 01 - Historian Hysteria")

	// ------------ File -------------

	/* <- File switch
	file, err := os.ReadFile("day01/inc/ex.txt")
	/*/ //
	file, err := os.ReadFile("day01/inc/in.txt")
	// --- End --- */

	check(err)

	// Added fix for Windows newline
	text := strings.ReplaceAll(string(file), "\r\n", "\n")
	//fmt.Println(text)

	// ----------- Setup -------------

	lines := strings.Split(text, "\n")

	col_a := make([]int, len(lines))
	col_b := make([]int, len(lines))

	for i, line := range lines {
		var a, b int
		_, err = fmt.Sscan(line, &a, &b)
		check(err)

		col_a[i] = a
		col_b[i] = b
	}

	slices.Sort(col_a)
	slices.Sort(col_b)

	part1 := part_one(col_a, col_b)
	part2 := part_two(col_a, col_b)

	// ----------- Output ------------

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

// -----------------------------------

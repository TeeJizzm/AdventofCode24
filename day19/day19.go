/* ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## */

// Day 19

// -----------------------------------

package main

// Imports
import (
	// Input/Output
	"fmt"
	"io/ioutil"

	// String manipulation
	"strings"
	//"strconv"
	// Other required imports
)

/* -----------------------------------
// Functions */

func part_one(lines []string) int {
	var part1 int = 0

	return part1
}

func part_two(lines []string) int {
	var part2 int = 0

	return part2
}

func main() {
	fmt.Println("Day 19 - *NAME*")

	// ------------ File -------------

	//*/ - File switch
	file, err := ioutil.ReadFile("ex.txt")
	/*/ //
	file, err := ioutil.ReadFile("in.txt")
	// --- End --- */

	if err != nil {
		fmt.Println(err)
	}

	// Added fix for Windows newline
	text := strings.ReplaceAll(string(file), "\r\n", "\n")
	fmt.Print(text)

	// ----------- Setup -------------

	lines := strings.Split(text, "\n")

	part1 := part_one(lines)
	part2 := part_two(lines)

	// ----------- Output ------------

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

// -----------------------------------

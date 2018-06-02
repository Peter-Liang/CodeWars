/*
7 kyu: Band name generator
https://www.codewars.com/kata/59727ff285281a44e3000011/train/go
*/

package kata

import "strings"

func bandNameGenerator(word string) string {
	if word[0] == word[len(word)-1] {
		return strings.Title(word + word[1:])
	}

	return "The " + strings.Title(word)
}

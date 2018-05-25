/*
8 kyu: Reversed Strings
https://www.codewars.com/kata/5168bb5dfe9a00b126000018
*/

package kata

import "strings"

func Solution(word string) string {
    var b strings.Builder
    b.Grow(len(word))
    for i := len(word) - 1; i >=0; i-- {
        b.WriteByte(word[i])
    }
    return b.String()
}

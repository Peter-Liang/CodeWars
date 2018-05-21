/*
7 kyu: Mumbling
http://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/go
*/

package kata

import (
	"strings"
)

func Accum(s string) string {
	res := make([]string, 0, len(s))
	for i, e := range s {
		cur := strings.Title(strings.ToLower(strings.Repeat(string(e), i+1)))
		res = append(res, cur)
	}
	return strings.Join(res, "-")
}

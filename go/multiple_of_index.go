/*
8 kyu: Multiple of index
http://www.codewars.com/kata/5a34b80155519e1a00000009/train/go
*/

package kata

func multipleOfIndex(ints []int) []int {
	result := make([]int, 0)
	for index, element := range ints[1:] {
		if element%(index+1) == 0 {
			result = append(result, element)
		}
	}
	return result
}

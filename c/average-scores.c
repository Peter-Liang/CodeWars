#include <stddef.h>
#include <math.h>

/*
 * 7 kyu: Average Scores
 * https://www.codewars.com/kata/average-scores/train/c
 */
int average(const int *values, size_t count){
  float total = sum(values,count);
  return round(total / count);
}

int sum(const int *values, size_t count){
    if (count == 1) {
        return values[0];
    }

    return values[count - 1] + sum(values, count - 1) ;
}

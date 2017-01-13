/*
6 kyu: Moves in squared strings (IV)
https://www.codewars.com/kata/moves-in-squared-strings-iv/train/typescript
*/
export class G964 {
    public static rot90Counter(strng: string) {
        const arr = strng.split('\n');
        let result: string[] = [];
        for (let col = arr.length - 1; col >= 0; col--) {
            let rowResult = ''
            for (let row = 0; row < arr.length; row++) {
                rowResult += arr[row][col];
            }
            result.push(rowResult);
        }
        return result.join('\n');
    }
    public static diag2Sym(strng) {
        const arr = strng.split('\n');
        let result: string[] = [];
        for (let col = arr.length - 1; col >= 0; col--) {
            let rowResult = ''
            for (let row = arr.length - 1; row >= 0; row--) {
                rowResult += arr[row][col];
            }
            result.push(rowResult);
        }
        return result.join('\n');
    }
    public static selfieDiag2Counterclock(strng) {
        const arr = strng.split('\n');
        const arr2 = G964.diag2Sym(strng).split('\n');
        const arr3 = G964.rot90Counter(strng).split('\n');
        let result: string[] = [];
        for (let i in arr) {
            result.push(arr[i] + "|" + arr2[i] + "|" + arr3[i]);
        }
        return result.join('\n');
    }
    public static oper(fct, s): string {
        return fct(s);
    }
}
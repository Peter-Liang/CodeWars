/*
6 kyu: A disguised sequence (I)
https://www.codewars.com/kata/a-disguised-sequence-i/train/typescript
*/
export class G964 {
    public static fcn(n: number): number {
        if (n == 0) return 1;
        if (n == 1) return 2;

        let u0 = 1, u1 = 2, u2: number, index = 1;
        while (index++ < n) {
            u2 = 6 * u0 * u1 / (5 * u0 - u1);
            u0 = u1;
            u1 = u2;
        }

        return u2;
    }
}
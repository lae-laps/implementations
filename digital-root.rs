/* Algorithm to calculate the digital root of a number

> Digital root -> the sum of the digits of a number untill the number of digits is equal to 0

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

*/

const RADIX: u32 = 36;

fn digital_root(n: i64) -> i64 {
    let mut s: String = n.to_string();
    while s.chars().count() != 1 {
        let mut v: Vec<i64> = Vec::new();
        for ch in s.chars() {
            let int = ch.to_digit(RADIX).unwrap();
            v.push(int as i64);
        }
        let sum: i64 = v.iter().sum();
        s = sum.to_string();
    }
    return s.parse().unwrap();
}

fn main() {
    let n: i64 = 942;
    let result: i64 = digital_root(n);
    println!("{} --> {}", n, result);
}

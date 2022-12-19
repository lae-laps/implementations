const RADIX: u32 = 10;

fn square_digits(num: u64) -> u64 {
    //todo!()
    let mut result: String = String::new();
    let bytes: String = num.to_string();
    for char in bytes.chars() {
        let x = char.to_digit(RADIX).unwrap();
        println!("{}", x);
        let square = x * x; 
        result = format!("{}{}", result, square)
    }
    return result.parse().unwrap()
}

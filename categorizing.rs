fn open_or_senior(data: Vec<(i32, i32)>) -> Vec<String> {
    let mut output: Vec<String> = Vec::new();
    for (age, handicap) in data {

        if age < 55 || handicap < 8 {
            output.push(String::from("Open"));
        } else {
            output.push(String::from("Senior"));
        } 
    }
    return output
}

fn main() {
    let data = vec![(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)];
    let result: Vec<String> = open_or_senior(data);
    println!("{:?}", result);
}

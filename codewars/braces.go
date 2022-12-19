package kata

func ValidBraces(str string) bool {
  for i, char := range str {
    if char == '[' {
      if str[i + 1] != ']' {
        return false
      }
    }
    if char == '{' {
      if str[i + 1] != '}' {
        return false
      }
    }
    if char == '(' {
      if str[i + 1] != ')' {
        return false
      }
    }
  }
  return true
}

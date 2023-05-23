
#include <stdio.h>

int solution(int number) {

	number--;

	if (number <= 0)
		return 0;
  
	int count = 0;
  
	for (int i = 1; i <= number / 3; i++) {
		int n = i * 3;
		if (n % 5 != 0)
			count += n;
	}
	for (int i = 1; i <= number / 5; i++) {
		count += i * 5;
	}
	return count;
}

int main() {
	for (int i = 1; i < 20; i++) {
		printf("%d > %d\n", i, solution(i));
	}
}

#include <stdio.h>
// Safe: uses parentheses to ensure correct precedence
#define MULTIPLY(a, b) ((a) * (b))

int main() {
    // Now correctly results in 25
    printf("Result: %d\n", MULTIPLY(2 + 3, 3 + 2));
    return 0;
}
#include <stdio.h>
// Unsafe: missing parentheses causes precedence issues
#define MULTIPLY(a, b) a * b

int main() {
    // This will result in 13 (2 + 3 * 3 + 2) instead of 25
    printf("Result: %d\n", MULTIPLY(2 + 3, 3 + 2));
    return 0;
}
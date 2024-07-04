#include <stdio.h>

int main() {
    char str1[] = "prime Hello";
    char str2[] = "World";

    printf("%s", str1 + str2[2] - str1[1]);

    return 0;
}
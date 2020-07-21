// > gcc -Wall -Wextra asciiz.c -o asciiz
// > asciiz

#include <stdio.h>
#include <string.h>

int main(void) {
    char my_string[128] = "My name is Alice";
    puts(my_string);

    my_string[11] = '\0';
    // Truncate the string to 11 characters.
    puts(my_string);

    // The strcat function is considered
    // unsafe at present because it does not
    // verify that the target buffer can hold
    // additional data. In this particular case,
    // of course, we know that sticking three
    // characters will not overflow the buffer,
    // but in the production quality code, we
    // should rather use the following safe
    //counterpart:
    //
    // strcat_s(my_string, sizeof(my_string), "Eve");
    strcat(my_string, "Eve"); // Sticking the sequence "Eve".
    puts(my_string);

    // An example of manual calculation of the string length.
    size_t my_string_len = strlen(my_string);
    size_t my_string_len_manual = 0;
    while (my_string[my_string_len_manual] != 0) {
        my_string_len_meanual++;
    }

    printf("strlen: %u\n"
           "manual: %u\n",
           (unsigned int)my_string_len,
           (unsigned int)my_string_len_manual);

    return 0;
}
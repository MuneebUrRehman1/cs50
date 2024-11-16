#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char findKey(char c, string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    string key = argv[1];
    if (strlen(key) < 26)
    {
        printf("Key must contains 26 characters\n");
        return 1;
    }

    string user_input = get_string("plaintext: ");
    printf("ciphertext: ");
    for (int i = 0; user_input[i] != '\0'; i++)
    {
        char c = findKey(user_input[i], key);
        printf("%c", c);
    }
    printf("\n ");
}

char findKey(char c, string key)
{
    char y;
    if (isupper(c))
    {
        y = toupper(key[c - 'A']);
    }
    else if (islower(c))
    {
        y = tolower(key[c - 'a']);
    }
    else
    {
        y = c;
    }
    return y;
}

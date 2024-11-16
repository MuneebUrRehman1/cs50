#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>


bool checkOnlyDigits(string str);
char rotate(char c, int k);

int main(int argc, string argv[])
{
    string num = 0;

    char ciphereText;

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if (!checkOnlyDigits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    string text = get_string("plaintext: ");

    int key = atoi(argv[1]);
    printf("ciphertext : ");
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            char c = rotate(text[i], key);
            printf("%c", c);
        }
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}

bool checkOnlyDigits(string str)
{
    return (isdigit(str[0]) || isdigit(str[1]));
}

char rotate(char c, int secret)
{
    string lower = "abcdefghijklmnopqrstuvwxyz";
    string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    char x;
    if (isupper(c))
    {
        x = upper[((c - 'A') + secret) % 26];
    }
    else
    {
        x = lower[((c - 'a') + secret) % 26];
    }
    return x;
}

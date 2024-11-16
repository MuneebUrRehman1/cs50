#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string str);
int count_sentenses(string str);
int count_words(string str);
int findGradeLevel(int letters, int words, int sentences);

int main(void)
{
    // index = 0.0588 * L - 0.296 * S - 15.8

    string str = get_string("Text: ");
    int letters_count = count_letters(str);
    int sentenses_count = count_sentenses(str);
    int words_count = count_words(str);
    int index = findGradeLevel(letters_count, words_count, sentenses_count);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string str)
{
    int count = 0;

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (isalpha(str[i]))
        {
            count++;
        }
    }

    return count;
}

int count_sentenses(string str)
{
    int count = 0;

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == '.' || str[i] == '!' || str[i] == '?')
        {
            count++;
        }
    }

    return count;
}

int count_words(string str)
{
    int count = 1;

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == ' ')
        {
            count++;
        }
    }

    return count;
}
int findGradeLevel(int letters, int words, int sentences)
{
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;

    return round(0.0588 * L - 0.296 * S - 15.8);
}

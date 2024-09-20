#include <cs50.h>
#include <stdio.h>

int find_underlined_sum(long card_number);
int find_non_underlined_sum(long card_number);
int find_length(long card_number);
int totalSum(int uncheckedSum, int checkedSum);
bool checkIsValidSum(int totalSum);
int checkStartingDigits(long card_number);

int main(void)
{
    long cardNumber = get_long("Number: ");

    int totalSum = find_underlined_sum(cardNumber) + find_non_underlined_sum(cardNumber);
    int length = find_length(cardNumber);
    bool isValidSum = checkIsValidSum(totalSum);
    while (cardNumber >= 100)
    {
        cardNumber /= 10;
    }
    int firstDigit = cardNumber / 10;
    int secondDigit = cardNumber % 10;
    int firstAndSecondDigits = (firstDigit * 10) + secondDigit;

    if (isValidSum)
    {
        if (length == 15 && (firstAndSecondDigits == 34 || firstAndSecondDigits == 37))
        {
            printf("AMEX\n");
        }
        else if (length == 16 && (firstAndSecondDigits == 51 || firstAndSecondDigits == 52 ||
                                  firstAndSecondDigits == 53 || firstAndSecondDigits == 54 ||
                                  firstAndSecondDigits == 55))
        {
            printf("MASTERCARD\n");
        }
        else if ((length == 13 || length == 16) && firstDigit == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

bool checkIsValidSum(int totalSum)
{
    if ((totalSum % 10) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int totalSum(int find_underlined_sum, int find_non_underlined_sum)
{
    return find_underlined_sum + find_non_underlined_sum;
}

int find_length(long card_number)
{
    long total_mod = 0;
    long divided_by = 10;
    int length = 0;
    while (total_mod != card_number)
    {
        total_mod = card_number % divided_by;
        divided_by *= 10;
        length++;
    }
    return length;
}

int find_underlined_sum(long card_number)
{
    long total_mod = 0;
    long divided_by = 100;
    int underline_sum = 0;
    while (total_mod != card_number)
    {
        total_mod = card_number % divided_by;

        int n = total_mod / (divided_by / 10);
        if (n != 0)
        {
            if (n * 2 >= 10)
            {

                underline_sum = underline_sum + (n * 2) % 10;
                underline_sum = underline_sum + ((n * 2) % 100) / 10;
            }
            else
            {
                underline_sum = underline_sum + (n * 2);
            }
        }

        divided_by *= 100;
    }
    return underline_sum;
}
int find_non_underlined_sum(long card_number)
{
    long total_mod = 0;
    long divided_by = 10;
    int non_underlined_sum = 0;
    while (total_mod != card_number)
    {
        total_mod = card_number % divided_by;
        int n = total_mod / (divided_by / 10);
        if (n != 0)
        {
            non_underlined_sum = non_underlined_sum + n;
        }

        divided_by *= 100;
    }
    return non_underlined_sum;
}

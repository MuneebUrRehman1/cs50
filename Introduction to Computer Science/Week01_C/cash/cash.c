#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int quarters = 25;
    int dimes = 10;
    int nickels = 5;
    int pennies = 1;

    int change_owed;
    int coins = 0;

    do
    {
        change_owed = get_int("Change owed: ");
    }
    while(change_owed<=0);


    coins += change_owed / quarters;
    change_owed %= quarters;

    coins += change_owed / dimes;
    change_owed %= dimes;

    coins += change_owed / nickels;
    change_owed %= nickels;

    coins += change_owed / pennies;
    change_owed %= pennies;

    printf("%i\n",coins);


}

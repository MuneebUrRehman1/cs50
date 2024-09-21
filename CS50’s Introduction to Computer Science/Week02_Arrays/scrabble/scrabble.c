#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
int computeScore(char str[]);
const char POINTS[] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                       1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int main(void)
{

    string player_01 = get_string("Player 1: ");
    string player_02 = get_string("Player 2: ");

    int player1_score = computeScore(player_01);
    int player2_score = computeScore(player_02);

    if (player1_score > player2_score)
    {
        printf("Player 1 wins!\n");
    }
    else if (player1_score < player2_score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int computeScore(char str[])
{
    int score = 0;
    int length = strlen(str);
    for (int i = 0; i < length; i++)
    {
        if (isalpha(str[i]))
        {
            score += POINTS[tolower(str[i]) - 'a'];
        }
    }
    return score;
}

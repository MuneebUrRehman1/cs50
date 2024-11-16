#include <stdio.h>
#include <cs50.h>

void printPyramids(int height);
int evaluateHeight();

int main(void)
{
    printPyramids(evaluateHeight());
    return 0;
}

int evaluateHeight()
{
    int height;
   do{
        height = get_int("Height: ");

    }while(height<1 || height >8);

    return height;
}

void printPyramids(int height)
{
    int space = height-1;
    for(int i=0; i<height; i++)
    {
         for(int k=0; k<space; k++)
        {
            printf(" ");

        }
        for(int j=0; j<=i; j++)
        {

            printf("#");
        }

        printf("  ");

        for(int j=0; j<=i; j++)
        {

            printf("#");
        }

        space--;

        printf("\n");
    }
}


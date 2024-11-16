#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avgColor = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3;
            image[i][j].rgbtBlue = avgColor;
            image[i][j].rgbtGreen = avgColor;
            image[i][j].rgbtRed = avgColor;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            int redSpeia = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int greenSepia = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int blueSepia = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            if (redSpeia > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = redSpeia;
            }
            if (greenSepia > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = greenSepia;
            }
            if (blueSepia > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = blueSepia;
            }
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int k = width;
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp;
            temp = image[i][j];
            image[i][j] = image[i][k - 1];
            image[i][k] = temp;
            k--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int totalRed = 0;
            int totalGreen = 0;
            int totalBlue = 0;
            int count = 1;
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int newK = i + k;
                    int newL = j + l;

                    if (newK >= 0 && newK < height && newL >= 0 && newL < width)
                    {
                        totalRed += image[newK][newL].rgbtRed;
                        totalGreen += image[newK][newL].rgbtGreen;
                        totalBlue += image[newK][newL].rgbtBlue;
                        count++;
                    }
                }
            }

            copy[i][j].rgbtRed = round((float) totalRed / count);
            copy[i][j].rgbtGreen = round((float) totalGreen / count);
            copy[i][j].rgbtBlue = round((float) totalBlue / count);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = copy[i][j];
        }
    }
    return;
}

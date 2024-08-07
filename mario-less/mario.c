#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // (note to self don't forget to assign variables)
    int n;
    do
    {
        // take user input
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    // for loops to make the pyramids
    // for the height
    for (int i = 0; i < n; i++)
    {
        // for the width
        for (int j = 0; j < n; j++)
        {
            // if, else conditions
            if (i + j < n - 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}
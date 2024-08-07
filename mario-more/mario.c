#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n, i, j, k, l;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    for (i = 0; i < n; i++)
    {
        // for the width
        for (j = 0; j < n; j++)
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
        printf("  ");
        for (j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
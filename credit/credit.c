#include <stdio.h>
#include <cs50.h>
#include <math.h>

bool luhnCheck(long cardNumber);
int getCardLen(long cardNumber);
void getCardProv(long cardNumber);

int main(void)
{
    long cardNumber = get_long_long("Card Number to Validate: ");
    if (luhnCheck(cardNumber) == true)
    {
        getCardProv(cardNumber);

    }
    else
    {
        printf("INVALID\n");
    }
}

bool luhnCheck(long cardNumber)
{
    int checkSum = 0;
    long tmp = cardNumber;

    for (int pos = 0; tmp > 0; pos++)
    {
        if (pos % 2 == 0)
        {
            checkSum += tmp % 10;
            tmp /= 10;
        }
        else
        {
            int odd = (tmp % 10) * 2;
            checkSum += (odd / 10 + odd % 10);
            tmp /= 10;
        }
    }
    return (checkSum % 10) == 0;
}

int getCardLen(long cardNumber)
{
    int len = log10(cardNumber);
    return len + 1;
}

void getCardProv(long cardNumber)
{
    int len = getCardLen(cardNumber);
    int prov;

    if (len == 16)
    {
        prov = (cardNumber / 1e14);
        if (prov >= 51 && prov <= 55)
        {
            printf("MASTERCARD\n");
        }
        else if (prov >= 40 && prov <= 49)
        {
            printf("VISA\n");
        }
        // For check error
        else
        {
            printf("INVALID\n");
        }
    }

    if (len == 13)
    {
        prov = (cardNumber / 1e12);
        if (prov == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

    if (len == 15)
    {
        prov = (cardNumber / 1e13);
        if (prov == 34 || prov == 37)
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (len <= 12 || len >= 17 || len == 14)
    {
        printf("INVALID\n");
    }
}
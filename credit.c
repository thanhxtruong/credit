#include <stdio.h>
#include <cs50.h>
#include <math.h>

#define AMEX 15
#define VISA1 13
#define MASTER_VISA 16

long long int cc_number;
int total_digits = 1;

int checksum(long long cc, int total);

int main(void)
{
    // Prompt user to input CC# and repeat until the correct input is received
    do
    {
        cc_number = get_long_long("Enter the credit card number: ");
    }
    while(cc_number <= 0 || cc_number == LLONG_MAX);

    long long temp = cc_number;

    // Calculate the total number of digits in the credit card #
    while((temp /= 10) != 0)
    {
        total_digits++;
    }

    // Check for valid total number of digits and determine card type based on the first 2 digits
    switch(total_digits)
    {
        case AMEX:
            // If the first 2 digits is either 34 or 37, check if checksum is valid
            if(cc_number / llround(pow(10, AMEX - 2)) == 34 || cc_number / llround(pow(10, AMEX - 2)) == 37)
            {
                if(checksum(cc_number, total_digits) == 0)
                    printf("AMEX\n");
                else
                    printf("INVALID\n");
            }
            // If the first 2 digits is not 34 nor 37
            else
                printf("INVALID\n");
            break;

        case VISA1:
            // If the first digit is 4, check if checksum is valid
            if(cc_number / llround(pow(10, VISA1 - 1)) == 4)
            {
                if(checksum(cc_number, total_digits) == 0)
                    printf("VISA\n");
                else
                    printf("INVALID\n");
            }
            // If the first digit is not 4
            else
                printf("INVALID\n");
            break;

        case MASTER_VISA:
            // If the total number of digits is 16 and the first digit is 4, this is not a Mastercard. Check if checksum is valid.
            if(cc_number / llround(pow(10, MASTER_VISA - 1)) == 4)
            {
                // If checksum is valid, this is a Visa
                if(checksum(cc_number, total_digits) == 0)
                {
                    printf("VISA\n");
                }
                // If checksum is NOT valid, this is not a Visa nor Mastercard
                else
                {
                    printf("INVALID\n");
                }
            }
            // If the total number of digits is 16 and the firs digit is NOT 4, this is not a Visa but could be a Mastercard
            else if(cc_number / llround(pow(10, MASTER_VISA - 2)) == 51 || cc_number / llround(pow(10, MASTER_VISA - 2)) == 52 || cc_number / llround(pow(10, MASTER_VISA - 2)) == 53 || cc_number / llround(pow(10, MASTER_VISA - 2)) == 54 || cc_number / llround(pow(10, MASTER_VISA - 2)) == 55)
            {
                if(checksum(cc_number, total_digits) == 0)
                    printf("MASTERCARD\n");
                else
                    printf("INVALID\n");
            }
            // If the first 2 digits is not 51, 52, 53, 54 nor 55
            else
                printf("INVALID\n");
            break;
        default:
            printf("INVALID\n");
    }
}

int checksum(long long cc, int total)
{
    // For every other digit starting at the second to last, multiply each digit by 2
    // If the result is greater than 9, add the 2 digits together before adding all the multiplication together
    // 2 3 5 1 6 8
    // | | | | | |
    // 5 4 3 2 1 0 (index i)
    int long long sum = 0;
    int digit;
    for(int i = 0; i < total; i++)
    {
        // If i is an odd number, multiply the digit by 2 first.
        // If the result is > 9, add the 2 digits togther until the result is less than 10
        // Then add the new digit to sum
        if(i % 2 > 0)
        {
            digit = (cc % 10) * 2;
            cc /= 10;
            while(digit > 9)
            {
                digit = (digit / 10) + (digit % 10);
            }
            sum += digit;
        }
        // If i is an even number, simply add sum to the new digit
        else if(i % 2 == 0)
        {
            digit = (cc % 10);
            sum += digit;
            cc /= 10;
        }
    }
    return(sum % 10);
}
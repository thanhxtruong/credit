#include <stdio.h>
#include <cs50.h>

// Prompt user to input CC#
int main(void)
{
    unsigned long long int cc_number;
    do
    {
        cc_number = get_long_long("Enter the credit card number: \n");
    }
    while(cc_number == ULLONG_MAX || cc_number <= 0);
    // Check for valid total number of digits and determine card type
    int total_digits = 0;
}
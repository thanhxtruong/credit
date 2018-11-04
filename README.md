# Credit card validation
This is problem set #6 in CS50<br/>
This program determines whether a provided credit card number is valid according to Luhn's algorithm. If the number is valid, the corresponding credit card company will be return, i.e. "AMEX", "VISA", "MASTERCARD". Otherwise, the program will print "INVALID"<br/>
# Background:
American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers.<br/>
merican Express numbers all start with 34 or 37; MasterCard numbers all start with 51, 52, 53, 54, or 55; and Visa numbers all start with 4. But credit card numbers also have a "checksum" built into them, a mathematical relationship between at least one number and others. That checksum enables computers (or humans who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow. (Consider the awkward silence you may have experienced at some point whilst paying by credit card at a store whose computer uses a dial-up modem to verify your card.) <br/>
Most cards use an algorithm invented by Hans Peter Luhn called "checksum", a nice fellow from IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:<br/>
1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products' digits together.<br/>
2. Add the sum to the sum of the digits that weren’t multiplied by 2.<br/>
3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!<br/>

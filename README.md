# Normal-Distribution-Getter
**A simple python program to get the normal distribution from any median and standard deviation.**

**Using tkinter GUI.**

## How use it?
This program need to be provided with at least 3 values: `Median`, `Standard Deviation` and a `Minimum Interval Value`. 

Optionally, the user can also provide a fourth value: the `Maximum Interval Value`, this value its only used when the "a < x < b" type of calculation its selected (Explained deeply below).

The program uses this user-given values aside 1800 random generated numbers (The aproximate equivalent to 5 years of data) to generate an estimated normal distribution

### Types of calculation: 
`"<"`: Every random number will be tested to be LESS than the `Minimum Interval Value`.

`"<="`: Every random number will be tested to be LESS OR EQUAL than the `Minimum Interval Value`.

`">"`: Every random number will be tested to be GREATER than the `Minimum Interval Value`.

`">="`: Every random number will be tested to be GREATER OR EQUAL than the `Minimum Interval Value`.

`"a < x < b"`: Every random number will be tested to be LESS than the `Minimum Interval Value` and GREATER than the `Maximum Interval Value`.

## Output
The output on the program will be displayed on the textbox in the footer of the window, in case of any problem present on the data given to the program, a error Messagebox will be displayed describing the problem ocurred.

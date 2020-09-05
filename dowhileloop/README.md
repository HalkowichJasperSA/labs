# Do-While loop

In this lab you will learn:

- What's the difference between a while and do-while loop
- How and when to use do-while loops

## What is a do-while loop?

The **do-while loop** is similar to a `while` loop in that it repeatedly executes a block of code as long as the condition you give it is `true`. However, a `while` loop checks its condition *first*, before executing the code block. The do-while loop though, will always execute at least once, and *then* check the condition to determine if it should execute again.

One example where this is useful is in validating user input. Say you want to prompt the user for a positive integer, and you want to reject negative numbers or zero. The CS50 `get_int()` function does a great job at rejecting inputs that are not `int`s, but you have to do your own checking for value.

```c
int positive_int;

do
{
  positive_int = get_int("Enter a positive int: ");
}
while (positive_int <= 0);
```

{% next %}

The condition here often seems counterintuitive. You want to accept a positive number, but the Boolean expression checks for numbers less than or equal to zero. The idea here is that you want the prompt to repeat when the input is *invalid*. So the loop needs to repeat as long as `(positive_int <= 0)` is `true`.

Note that we are declaring our variable, `positive_int`, outside of the loop. A variable declared in a loop has a scope limited to the curly braces that surround it, meaning its value is only available inside the loop.

Note also that there is a semicolon `;` after the condition, since this is the end of the do-while statement.

{% next %}

## Your Turn

Complete the program to the right to include a do-while loop to validate user input. The program should only accept a number between *1* and *10* inclusive.

Be sure to test your program with numbers in this range, numbers outside of this range, as well as zero, negative numbers, and floating point numbers.

Hint: you may have to use a logical operator, such as `&&` (AND) or `||` (OR) to combine two conditions for this.

[For more info on loops, download the CS50 Loops Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/loops.pdf)

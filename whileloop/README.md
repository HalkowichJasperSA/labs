# `while` loop

In this lab you will learn:

- What is a `while` loop
- How and when to use `while` loops

## What is a while loop?

The **while loop** repeatedly executes a block of code as long as a given condition is true. You typically use a while loop when you don't know in advance how many times you want a block of code to repeat. An example might be to determine how many times a number can be divided by 2:

```c
int n = get_int("Enter a number: ");
int count = 0;

while (n > 1)
{
    n = n / 2;
    count++;
}

printf("Your number can be divided by 2 %i times\n", count);
```

{% next %}

The syntax for a `while` loop is similar to an if statement, with the key word `while` replacing the `if`. The condition is given in parentheses and the block of code to execute is wrapped in curly braces `{}`. Though the syntax is similar, the execution is different. The `while` loop repeatedly executes the block of code as long as the condition is true. The `if` statement executes the block of code only once if the condition is true.

## Forever loop

You can use a `while` loop in C to create a "forever", or *infinite*, loop:

```c
while (true)
{
    printf("hello, world\n");
}
```

The loop will check whether the expression evaluates to true (which it always will in this case), and then run the lines inside the curly braces. This loop will repeat infinitely until you explicitly tell the program to break out of it.

{% next %}

## Your turn

Complete the program on the right to create a loop that determines how many times you can double a number before it reaches 100.

Then test your code, as you did in previous labs, with valid inputs, invalid inputs, and corner cases. One corner case you might try is an input of zero. What do you think will happen?

{% spoiler "Does your program seem to hang?" %}

When you enter a zero for input, you can double that number forever, and the result is still zero! The condition you wrote is always going to be true! Because of this, your loop runs forever, giving the appearance of your program hanging. You can stop the program by pressing `ctrl + c`.

{% endspoiler %}

What happens when you enter a negative number?
{% spoiler "Not sure what the strange error message means?" %}

You'll probably see something like:
```
runtime error: signed integer overflow: -2147483648 * 2 cannot be represented in type 'int'
```

Remember that the smallest value an `int` can hold is *-2<sup>31</sup>* (*-2147483648*), so when you try to store a value smaller than this, you end up with an **integer overflow** error.

{% endspoiler %}

[For more info on loops, download the CS50 Loops Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/loops.pdf)

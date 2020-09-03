# `for` loop

In this lab you will learn:

- The purpose of a for loop
- How to use it

## What is a `for` loop?

The **for loop** is probably the most frequently used of the three types of loops. It's very useful when you want to repeat something a known number of times.

You'll see how they can be useful for:

* Repeating a block of code *10*, *20*, or *n* times when you know in advance the value of *n*
* Accessing each individual character in a string
* Looking at each element in an array (more on this in later lessons)

Let's start by taking a look at the analogous loop in Scratch.

{% next %}

![scratch_repeat](https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/forloop/repeat.png)

can be recreated in C by:

```c
for (int i = 0; i < 50; i++)
{
    printf("hello, world\n");
}
```

A for loop has three parts (included in parentheses after the word for, and separated by semicolons)

* **Initialization**: `int i = 0` is an initialization of the `int` variable `i`, which means that we created a variable and set its initial value to 0. `i` is a conventional name for a counting variable, but you are free to use any variable name you like.

* **Loop Condition**:  `i < 50` is the Boolean expression that the loop checks to determine if it will continue. When this condition is `true`, the loop will run the code inside the curly braces. Since `i` started at 0, stopping before `i` reaches 50 will mean this loop repeats exactly 50 times, intended.

* **Increment Statement**:  This statement is executed at the end of every loop. In this case, it increases the value of `i` by *1* before continuing to the next iteration.

{% next %}

Since the loop variable is an ordinary variable, you can use it in the loop. Consider the following code:

```c
for (int j = 1; j <= 10; j++)
{
    printf("%i\n", j);
}
```

Can you see what this loop will print? Feel free to try it out by typing the code and compiling it on the right. What is the difference between using `j <= 10` and `j < 10` for the loop condition.

{% next %}

## Your turn

Modify the code on the right to sum the numbers from 1 to 10, using either the supplied for loop or creating your own. Store the total in a variable named `total`.

{% spoiler "Hint" %}

Keep in mind that you can use the value of `i` in your calculation. You can also change the loop to start at one and end when `i <= 10`. This gives you a value which can be added to `total` during each iteration.

{% endspoiler %}

[For more info, download the CS50 Loops Reference Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/loops.pdf)

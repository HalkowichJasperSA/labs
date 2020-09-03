# Functions

In this lab you will learn:

- What is a function
- Why programmers use functions
- How to write your own functions in C

## What is a function?

**Functions** in programming are similar to those we've seen in math, in that they take in some input and produce some output.

Since the first program you wrote, you've been using functions. These were functions that were supplied to you, and you didn't have to create yourself, such as `printf()`, `get_int()`, and even `main()`.

These functions were written by programmers many years ago, and are made available so you don't have to constantly reinvent the wheel.

Imagine what programming would be like if you had to recreate `printf()` every time you wanted to output something to the terminal window. It would take forever to complete the simplest program!

The other reason that programmers use functions is **abstraction**. To use `get_int()` for example, you need to know:

* The name of the function
* What the function does
* What arguments to give to the function
* What kind of result the function returns

In order to use `get_int()`, you don't have to know how it's implemented. You only need to know how to use it.

{% next %}

## Writing your own functions

You can write our own functions as well. Once you've taken the time to program and debug your function, you can use it over and over in multiple programs. Using functions, your code becomes simpler, more organized, and easier to debug.

Every C program that you've written so far contains one function, the `main()` function. You can define our own custom functions with similar syntax.

In order to use your own custom function, we need to give the compiler information about the function. You do this by placing a function **prototype** above the `main()` function.

The prototype contains three parts:

1. The **return type**, which is the data type of the function's output. The return type of the `get_int()` function, for instance, is an `int`. Sometimes a function does not return a value, (such as `printf()`), in which case the return type is `void`.
2. The name - this cannot include spaces and cannot be one of C's existing keywords.
3. The parameters, in parentheses, also known as **arguments**. These are the function's inputs (if there are none, use `void`). The data type of each argument must be included in front of the argument's name.

The function definition includes the logic that will be carried out, enclosed in curly braces. The function definition typically follows the `main()` function. Note that the function prototype is followed by a semicolon, `;`, while the function definition is not.

{% next %}

Let's take a look at this example:

```c
#include <cs50.h>
#include <stdio.h>

int square(int n);

int main(void)
{
    int side = get_int("Enter the side length: ");
    printf("The area is %i.\n", square(side));
}

int square(int n)
{
    return n * n;
}
```

This code defines a custom function named `square()`. The function has a return type (`int`), a name (`square`), and an argument with its type (`int n`). The `main()` function calls the `square()` function when printing the square of the input.

When the function runs, the value passed when it's called (stored in `side`) is copied into the input variable (aka parameter) of the function (`n`). Finally, it returns its result, which must be an `int` since the function was declared with an `int` return value.

Note that `square()` is defined after the `main()` function. Placing the function prototype before `main()` allows the compiler to recognize it before `main()` calls it.

Feel free to try typing this code into a new file, compiling it, and testing it.

{% next %}

## Your Turn

Now you will create a custom function called `get_positive_int()`. It should take as input a prompt from the user and should output only a positive integer. You may want to use functions we've already used, such as `get_int()`, in your implementation.

The prototype, return type (`int`), the function name (`get_positive_int`), and the input argument (`prompt`), which has a `string` datatype, are already defined for you. Your job is to implement the function so that it continues to prompt the user until they provide a positive integer.

{% spoiler "Hint" %}
Think back to the lab where you used a loop to validate user input. Can using a do while loop work here?
{% endspoiler %}

Try to get the function to do one thing at a time. Perhaps get a loop working without a `prompt` first, that only accepts positive numbers. Then try to add the `prompt`.

{% spoiler "Hint for using `prompt`" %}

If you want to use `get_int()`, using `prompt` directly inside the parentheses won't work. This is because the input for `get_int()` works like a `printf()` statement, where we use placeholder for variables. So you may need syntax like

```c
result = get_int("%s", prompt);
```

to use the parameter with `get_int()`.

{% endspoiler %}

If you are really stuck, try to write some pseudocode first.

{% spoiler "Need help with the pseudocode?" %}

1. Declare a new variable to store the user input.
2. Get a value from the user and store in your new variable.
3. Check to see if the value of this variable is less than or equal to zero.
    1. If it is, go back to step 2.
4. Return the value that we know now is a positive number.


{% endspoiler %}


[For more information on functions download our CS50 Functions Reference Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/functions.pdf)

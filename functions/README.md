# Functions

In this lab you will learn:

- What is a function
- Why programmers use functions
- How to write your own functions in Python

## What is a Function?

**Functions** in computer science are similar to those you've seen in math: they take in some input and produce some output.

Since the first program you wrote, you've been using functions! These were functions that were given to you, that you didn't have to create ourselves, such as `print()` and `range()`.

These functions were written by programmers many years ago, and are made available to you so you don't have to constantly reinvent the wheel! You're able to reuse these functions over and over again.

Imagine what programming would be like if you had to recreate `print()` every time you wanted to output something to your terminal window! It would take forever to complete the simplest program!

The other key reason that programmers use functions is **abstraction**. To use `input()` for instance, we need to know

* The name of the function
* What the function does
* What arguments to give to the function
* What kind of result the function returns

In order to use `input()`, you don't have to know how it's implemented. You only need to know how to use it.

{% next %}

## Writing our own functions

You can write your own functions as well! Once you've taken the time to program and debug your function, you can use it over and over again in multiple programs. Using functions, your code becomes simpler, more organized, and easier to debug!

Let's take a look at this example:

```python
def square(n):
    return n * n

side = int(input("Enter the side length: "))
print(f"The area is {square(side)}.")
```

Here, we've defined a custom function named `square()`. The function has a name, `square`, and an **argument**, `n`. The main part of the program calls the `square()` function when printing the square of the input.

When the function runs, the value that is passed when it's called (stored in `side`) is copied into the variable defined as an input to the function (`n`). We now calculate the square and return its value.

Feel free to try typing this code into a new file and testing it.

{% next %}

## Your Turn

Now you will create a custom function `f_to_c()`, that should accept a float parameter (the temperature in Fahrenheit) and return the equivalent temperature in Celsius.

The code is already started, with a function already defined. However the function itself always returns 0.

Your job is to implement the formula for converting Fahrenheit to Celsius:

```
C = (F - 32) * 5 / 9
```

Example of running the program:

```
$ python functions.py
Temp in F: 68
Temp in C: 20
```

{% next %}

### How to Check Your Code

Once you've tested the program yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to always test it yourself as well!

```
check50 scienceacademy/problems/2021/7/functions
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 functions.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/functions
```

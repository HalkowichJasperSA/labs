# For Loop

In this lab you will learn:

- What is a for loop
- How to use a for loop

## What is a For Loop?

The **for loop** is probably the most frequently used loop of the two types of loops. It is very useful when you want to repeat something a *known number of times*.

You'll see how for loops can be useful for:
* Repeating a block of code 10 or 20 or *n* times when you know in advance the value of *n*
* Accessing each individual character in a string
* Looking at each element in an list (more on this to come later!)

Let's start by taking a look at an example:

```python
for i in range(10):
    print("hello, world")
```

A for loop has three parts (which come after the word `for`):

* **Loop variable**: This variable keeps track of how many iterations the loop has already done. `i` is a common name for a counting variable.

* **Loop sequence**: Next comes a sequence of values that the loop variable will get. `range()` is one way of making this sequence. `range(10)` means "make a list of the numbers up to 10". This is how many times the loop will repeat.

* **Loop block**: This is the code that comes after the `:` (note that it is indented). This is one or more statements that will be executed every time the loop repeats.

{% next %}

By using the loop variable, you can also get a loop to do something slightly different each time the loop repeats, or iterates.

For example, let's look at the following code:

```python
for i in range(10):
    print(i)
```

`range(10)` produces a list of the numbers up to 10 (`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`) and the for loop sets `i` to each one of them, one at a time. Therefore, when you run this code, it will print all of the numbers from 0 through 9.

{% next %}

## Other things you can do with `range()`

You can also give additional *parameters* to `range()` to choose the start, end, and step values of the numbers. For example, to count by threes:

```python
for i in range(0, 21, 3):
    print(i)
```

Or to count backwards from 10 down to 1:

```python
for i in range(10, 0, -1):
    print(i)
```

{% next %}

## Your Turn

Modify the code on the right to add up the numbers from 1 to 10, using either the supplied for loop or creating your own. Store the total in the variable named `total`.

{% spoiler "Hint" %}

* Remember, you can set a new variable using `=`:

```
total = 0
```

* You can use the value of `i` in your calculation.

```
total = total + i
```

* Don't forget to print out your result at the end:

```
print(total)
```

{% endspoiler %}

{% next %}

### How to Check Your Code

Once you've tested the program yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to always test it yourself as well!

```
check50 scienceacademy/problems/2021/7/forloop
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 forloop.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/forloop
```


# Data Types

In this lab you will learn about:

- The common data types used in programming
- Problems that can arise with `ints` and `floats`
- Data input functions for different data types

## What is a Data Type?

A **data type** is a classification that specifies what kind of value a variable represents. A `string` holds textual data, while an `int` is a whole number.

The Python programming language is a **dynamically-typed** language. A variable's type is determined by what is assigned to it.

{% next %}

## Native Data Types

Let's start with the data types used most frequently.

### int

An `int` is a data type which represents an **integer**: its value could be a positive or negative whole number, or zero. Numbers like 5, 28, -3, and 0 can be represented as ints, but numbers like 2.8, 5.124, and -8.6 cannot.

Recall that whenever you ask for user input with `input()`, the result is a string. To convert that input to an integer, you can write:

```python
age = int(input("Enter your age: "))
```

{% next %}

### float

To store numbers that are not whole numbers, Python uses a data type known as a `float`, for **floating-point** number. A float stores negative and positive numbers that contain decimals, such as 5.12 or -17.32.

Since there are an infinite number of numbers with decimals, and the computer has a finite number of bits, the computer cannot represent every floating point number with 100% accuracy. This can be a problem when more accuracy is needed. This problem is called **floating-point imprecision**.

Example of inputting a float:

```python
change = float(input("Enter dollars and cents: "))
```

{% next %}

### string

The `string` data type holds **text**.

Strings in Python must be surrounded by quotes, either double (`"`), or single (`'`) - as long as you use the same kind on both ends. For instance:

```python
name = "Zelda"
```

To have a user input string data, you don't need to convert anything at all:

```python
name = input("Enter your name: ")
```

### bool

A `bool` is a *boolean value*: a data type that stores one of only two possible values: **True** or **False**. We use bools to control the flow of our code.

For instance:

```python
game_started = True
game_finished = False
```

{% next %}

## Practice Using These Data Types

In the text editor to the right, you will see **comments** (lines starting with `#`) explaining what each missing line of code should be doing. Your job is to complete this missing code, to get user input for each of these data types shown above.

The first of these is already done for you.

Be sure to use the same variable names as the comments suggest, so that `print()` works properly to print out these values later on in the program.

When you are done, **execute** your code by typing:

```
python datatypes.py
```

at the `$` prompt.

If you see any errors, try to look for hints in the rather cryptic hints given.

{% next %}

### How to Check Your Code

Once you've tested the program yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to always test it yourself as well!

```
check50 scienceacademy/problems/2021/7/datatypes
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 datatypes.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/datatypes
```


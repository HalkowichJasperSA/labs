# Boolean Expressions and Conditionals

In this lab you will learn:

- How to use Boolean expressions in Python
- Why and how to combine Boolean operators
- Why conditional statements are so important

## What are Boolean Expressions?

A **Boolean expressions** is one that has a value of either **True** or **False**.

**Boolean operators** are the comparison operators that we use in Boolean expressions: `<` (less than), `>` (greater than), `==` (equal to), `<=` (less than or equal to), `>=` (greater than or equal to), and `!=` (not equal to).

{% next %}

## Conditional Statements

### The `if` Statement

We use boolean expressions with **if statements** to execute different parts of code, depending on different circumstances. For example:

```python
if x < y:
    print("x is less than y")
```

In our code, we assume that `x` and `y` have already been initialized or set to some other values beforehand.

We use indentation to indicate the lines of code that will run if the statement is true.

{% next %}

We also have **if-else** statements which will execute either one branch or the other:

```python
if x < y:
    print("x is less than y")
else:
    print("x is not less than y")
```

The `else` captures all cases that don’t match the first condition.

{% next %}

And finally we can have more than two branches by combining multiple **if-else** statements:

```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

To compare two values, you use `==`, two equal signs. Remember from previous labs that the single `=` sign represents assignment.

{% next %}

## Combining Boolean Expressions

We can combine Boolean expressions by using the **logical operators**.  `and` will evaluate to `true` if both expressions on either side of it are true. `or` evaluates to `true` if at least one of the two expressions on either side is true. And `not` evaluates to the opposite of whatever the expression after it evaluates to.

We can now execute a block of code only if multiple conditions are true as in:

```python
if age > 12 and age < 20:
    print("You are officially a teenager!")
```

{% next %}

## Grades

You have two problems to solve in this lab. First, let's look at `grades.py`.

If you try to run the code in `grades.py` on the right, you'll see there's a problem. If the user inputs `95`, all four statements print out!

```
$ python grades.py
Enter your grade (between 60 and 100): 95
You got an A!
You got a B!
You got a C!
You got a D!
```

Fix the program so that only the correct statement prints out.

Make sure to test your code by entering a variety of numbers between 60 and 100.

{% next %}

## Even or odd

Now look at `odd_even.py`. This program asks the user to input a number.

Your task is to print "Odd" or "Even" depending on the number that was entered. When you run the program, it should look like this:

```
$ python odd_even.py
Enter a number: 7
Odd

$ python odd_even.py
Enter a number: 6
Even
```

Don't forget to test your code and make sure it outputs the right response!

{% next %}

### How to Check Your Code

Once you've tested the programs yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to always test it yourself as well!

```
check50 scienceacademy/problems/2021/7/conditionals
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 grades.py
```

and

```
style50 odd_even.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/conditionals
```

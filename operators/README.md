# Operators

In this lab you will learn:

- How math operators work in Python
- How and when to use the remainder operator
- The different ways of using assignment operators

## Arithmetic Operators

The addition (`+`), subtraction (`-`), multiplication (`*`), and division ('/') **operators** work the same way in Python as they do in your math class. No big surprises here.

You can write `10 * 3` and of course the result would be *30*.

You can use these operators with numbers or variables. If you've already assigned the value *10* to an integer variable `a`, you would get the same result by writing:

```python
a * 3
```

{% next %}

However, this is not storing the resulting value of *30* in anything. The value of `a` is not changed. Its value is just used as part of the calculation.

If you wanted to store the result of this calculation in a new integer variable, `b`, you could write:

```python
b = a * 3
```

In order to change the value of `a` to be equal to 3 times itself, your code could look as follows:

```python
a = a * 3
```

{% next %}

## Modulo

An operator in most programming languages that you may not have seen before is the remainder, or **modulo** operator. The symbol used by modulo is the `%` sign, and an operation using modulo looks like this:

```python
remainder = 5 % 2
```

Since 2 goes into 5 twice with a remainder of one, the result is 1.

Though it may not be obvious at first, this operator can be very useful in programming. It can tell you if a value is divisible by a number, and as we'll see later can be used as a "wrap around" operator, where numbers wrap around back to zero after reaching a certain value.

{% next %}

## Assignment Operators

You've already seen the assignment operator `=`. This evaluates the expression on the right side of the statement, and assigns it to the variable on the left.

There are a few shortcuts for assignment that you'll soon encounter as well.

| Symbol     | Example      | Result |
| ------------- |------------------| ------- |
| `+=`           | `a += 2`           | sets `a` to 2 plus the current value of `a`|
| `-=`           | `a -= 2`           | sets `a` to 2 minus the current value of `a`|
| `*=`          | `a *= 2`            | sets `a` to 2 times the value current of `a`|
| `/=`          | `a /= 2`            | sets `a` to 2 divided by the current value of `a`|


{% next %}

## Your turn!

The program on the right is partially completed. It asks for user input and assigns it to an `int` variable `a`. Your job is to declare more variables, as directed by the comments, and use the appropriate operator to assign the proper value.

Execute your code by typing this command in the terminal:

```
python operators.py
```

### How to Check Your Code

Once you've tested the program yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to always test it yourself as well!

```
check50 scienceacademy/problems/2021/7/operators
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 operators.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/operators
```

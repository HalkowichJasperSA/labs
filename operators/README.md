# Operators

In this lab you will learn:

- How math operators work in C
- How to use the remainder operator
- Different ways of using assignment operators

## Arithmetic operators

The addition (`+`), subtraction (`-`), and multiplication (`*`) **operators** work the same way in C as they do in your math class.

You can write `10 * 3` and as expected the result would be *30*.

You can use these operators with numbers or variables. If you've already assigned the value *10* to an integer variable `a`, you would get the same result by writing:

```c
a * 3;
```

{% next %}

Note this is not storing the resulting value of *30* anywhere. The value of `a` is not changed. Its value is just used as part of this calculation.

If you wanted to store the result of this calculation in a new integer variable, `b`, you could write:

```c
int b = a * 3;
```

To change the value of `a` to be equal to 3 times itself, you could do this:

```c
a = a * 3;
```

Notice that  you didn't write `int` in front of the `a` in this last example. Why? Since `a` must have already had a value, it must have already been declared earlier in your program!

{% next %}

## What about division?

You'll notice that division wasn't mentioned in the section above. The symbol used for division is `/`. However, division in C works differently when you are dividing ints than you might expect.

If you write:

```c
5 / 2;
```

you are telling your program to divide two ints. Remember, ints can only hold whole numbers. This means the operation of dividing two ints will truncate, or cut off, everything after the decimal point. The result of this operation is therefore *2*!

If doesn't matter if you try to store this in an `int` or a `float`. The result of the operation will be evaluated first, and then assigned to your variable.

If you wanted to save the output of this calculation:

```c
int a = 5 / 2;
```

the value of `a` will be *2*.

{% next %}

If you save the output of this calculation to a `float`:

```c
float b = 5 / 2;
```

the value of `b` will be *2.0*.

When at least one of the numbers in your division statement is a `float`, C will interpret this as dividing two floats. So:

```c
float b = 5.0 / 2;
```

will assign *2.5* to `b`.


Now if you write:

```c
int a = 5.0 / 2;
```

think about what happens: the division results in a `float`, but now this value is assigned to an `int`, so again, everything after the decimal point gets truncated, and `a` gets the value *2*.

{% next %}

# Modulo

An operator in most programming languages that you may not have seen before is the remainder, or **modulo** operator. The symbol used by modulo is `%`, and an operation using modulo looks like this:

```c
int remainder = 5 % 2;
```

Since 2 goes into 5 twice with a remainder of one, `remainder` is *1*.

Though it may not be obvious at first, this operator can be very useful in programming. It can tell you if a value is divisible by a number, and as you'll see later can be used as a "wrap around" operator, where numbers wrap around back to zero after reaching a certain value.

> Note: Modulo can only be used with ints.

{% next %}

## Assignment Operators

You've already seen the assignment operator `=`. This evaluates the expression on the right side of the statement and assigns it to the variable on the left.

There are a few shortcuts for assignment that you'll soon encounter as well.

| Symbol     | Example      | Result |
| ------------- |------------------| ------- |
| `++`           | `a++;`    | increases the value of `a` by *1* |
| `--`         | `a--;`   | decreases the value of `a` by *1* |
| `+=`           | `a += 2;`           | increases the value of `a` by *2* |
| `-=`           | `a -= 2;`           | decreases the value of `a` by *2* |
| `*=`          | `a *= 2;`            | multiplies `a` by *2* |
| `/=`          | `a /= 2;`            | divides `a` by *2* |


{% next %}

## Your turn!

The program on the right is partially completed. It asks for user input and assigns it to an `int` variable `a`. Your job is to declare additional variables according to the comments, and use the appropriate operator to assign the proper value.

<!--
{% spoiler "Doug's video on operators" %}
{% video https://www.youtube.com/watch?v=f1xZf4iJDWE %}
Note: Boolean operators will be discussed in the Boolean Expressions Lab.
{% endspoiler %}
-->

[Download the CS50 Reference Sheet on Operators](https://cs50.harvard.edu/ap/2020/assets/pdfs/operators.pdf)

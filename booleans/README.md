# Boolean expressions and conditionals

In this lab you will learn:

- How to use Boolean expressions in C
- Why and how to combine Boolean operators
- Why conditional statements are so important

## What are boolean expressions?

A **boolean expressions** is one that has a value of either **true** or **false**.

**Boolean operators** are the comparison operators that we use in Boolean expressions: `<` (less than), `>` (greater than), `==` (equal to), `<=` (less than or equal to), `>=` (greater than or equal to), and `!=` (not equal to).

{% next %}

## Conditional statements

### The `if` statement

You use boolean expressions with **if statements** to execute different parts of code, depending on different circumstances.  For example:

```c
if (x < y)
{
    printf("x is less than y\n");
}
```

will only print "x is less than y" if the condition (`x < y`) is `true`.

{% next %}

There are also **if-else** statements which will execute either one branch or the other:

```c
if (x < y)
{
    printf("x is less than y\n");
}
else
{
    printf("x is not less than y\n");
}
```

`else` captures all conditions that don't match the first one.

{% next %}

You can have more than two branches by nesting **if-else** statements:

```c
if (x < y)
{
    printf("x is less than y\n");
}
else if (x > y)
{
    printf("x is greater than y\n");
}
else if (x == y)
{
    printf("x is equal to y\n");
}
```

Note that in C, to compare two values, we need to use `==`.

{% next %}

### The ternary operator

The **ternary operator** is a third type of condition. The ternary operator takes an expression, and evaluates to one value if the expression is `true`, and another value if it is `false`.

For example, if we want to set the variable `min` to either `a` or `b` depending on which has the lower value (assuming that all three variables have already been declared, and that `a` and `b` have assigned values) we could write:

```c
if (a < b)
{
    min = a;
}
else
{
    min = b;
}
```

or we can use the ternary operator and write:

```c
min = (a < b) ? a : b;
```

which says if `a < b` is true, then set `min` to `a`, else set `min` to `b`.

{% next %}

## Combining Boolean expressions

You can combine Boolean expressions by using the **logical operators**.  `&&` is the logical **AND** operator: it will evaluate to `true` if both expressions are `true`. `||` is the logical **OR** operator: it evaluates to `true` if at least one of the two expressions on either side is `true`. And `!`, the logical **NOT** operator, evaluates to the opposite of whatever the expression after it evaluates to.

```c
if (age > 12 && age < 20)
{
    printf("You are officially a teenager!\n");
}
```

Note that the the two conditions are combined inside of the parentheses.

## Your turn

Complete the code on the right by adding one or more conditional statements to print out only one phrase, depending on the grade that's input.

Then test your code by entering inputs that are ints, floats, or strings. Don't forget to try values outside the expected range (like *1000*)!

[For more info, download the CS50 Boolean Expressions Reference Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/boolean_expressions.pdf)

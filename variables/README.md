# Variables

In this lab you will learn about:

- The difference between variables in math and programming
- Creating and naming a variable
- Assigning a value to a variable

## What is a variable?

In computer programming, a **variable** is a container that holds numbers, words, or other types of data in your program. Variables in programming are similar to the variables you use in math class, since they both represent a value. Unlike variables in math, variables in programming do not represent an "unknown", and hold values that can change as the program executes.

Another difference is in variable names. In math, variables are typically only one letter long, as in *x*, or *y*, or *n*. In most programming languages, variable names can be a single letter, a word, or even a phrase (as long as there are no spaces). In fact, it's considered good programming practice to use variable names that describe the data they are storing.

For instance, you might store a name in a variable `name`, and an age in a variable `age`. You can combine multiple words with underscores, such as `student_name`, and `teacher_name`. But if you create a variable name with a space in it, such as `student name`, your program won't understand what you want it to do.

{% next %}

## Declaring a variable

In the C programming language, you have to **declare** a variable before you can use it. You do this by telling the program the type of data your variable will hold, followed by the name of the variable, as in:

```c
int age;
```

This declares the variable `age` as an integer, meaning it can only hold whole numbers.

If you try to use a variable before declaring it, you'll generate an error when you try to compile your program.

{% next %}

## Assigning a value to a variable

To store a number in the variable you just declared you can write:

```c
age = 18;
```

The `=` sign here is *not* the same `=` from your math class. In programming, `=` means **assignment**, not equality. It says to the computer: "Assign *18* to the storage location labeled `age`".

Assignment always works from right to left. In other words, the value on the right side of the `=` is evaluated first, then stored in the variable on the left side.

Something that may look strange to most people who start programming for the first time is an expression like:

```c
age = age + 1;
```

In Algebra, you'd attempt to solve for `age`, and this would be impossible. How can age equal itself plus one?

But if you remember that the `=` represents assignment, and not equality, you can read this as: "add one to the current value stored in `age`, then reassign this new value to `age`".

Keep in mind when you write a statement like this, you must have already assigned an initial value to `age`. For example:

```c
int age;
age = age + 1;
```

will generate an error, because `age` is declared, but doesn't have a value when you try to add one to it.

[For more info on variables, download the CS50 Variables Reference Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/variables.pdf)


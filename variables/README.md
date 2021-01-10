# Variables

In this lab you will learn about:

- The difference between variables in Math and CS
- Creating and naming a variable
- Assigning a value to a variable
- Getting user input for a variable

## What is a Variable?
In computer programming, a **variable** is a container that holds numbers, words, or other types of data to use in your program. Variables in programming are similar to the variables we use in math class, since they both represent a value. Unlike variables in math, variables in programming do not represent an "unknown", and hold values that can change as the program executes.

Another difference is in variable names. In math, variables are only one letter long, as in *x*, or *y*, or *n*. In most programming languages, variable names can be a single letter, a word or a phrase (as long as there are no spaces). In fact, it's considered good programming practice to use variable names that represent the data they are being used to store.

For instance, we might store a name in a variable `name`, and an age in a variable `age`. We can combine multiple words with underscores, such as `student_name`, and `teacher_name`. But if we create a variable name with a space in it, such as `student name`, our program won't understand what we want it to do!

{% next %}

## Assigning a Value to a Variable

To store a number in a variable you can write:

```python
age = 18
```

The `=` sign here works differently than it does in your math class. In programming, `=` means **assignment**, not equality. It says to the computer: assign `age` the value of 18.

Assignment always works from right to left. In other words, the value on the right side of the `=` is evaluated first and then stored in the variable whose name is on the left side of the `=`.

One thing that look strange to most people who start programming for the first time, is an expression like:

```python
age = age + 1
```

In math class, we know this can never be true! How can age equal itself plus one?

But if you remember that the `=` represents assignment, and not equality, you can read this as: "evaluate the result of adding one to the value stored in `age`, then reassign this new value to `age`".

Keep in mind when we write a statement like this, we must have already assigned an initial value to `age`. In other words, if your whole program contained:

```python
age = age + 1
```

it will generate an error, because `age` does not have a value when you try to add one to it.

Instead, assign a starting value to `age` and *then* increase it by one:

```python
age = 18
age = age + 1
```

{% next %}

## Getting User Input

So you've seen how you can code values into a variable by typing them into your program, but what if you want a use a different value for a variable each time you run it?

In this case you can use Python's `input()` function to prompt for a value in the terminal.

**IMPORTANT:**

There are many things a user could type, so by default anything captured with `input()` is represented as a **string**.

Since `age` needs to be an int, you can use `int()` to convert the value like this:

```python
age = int( input("Enter Your Age: ") )
```

The function `input()` takes an argument, which is the text that you want to prompt the user with.

{% next %}

## Now It's Your Turn!

Though the program on the right is correct and will execute properly, it is not well designed. For one thing, what if you want to start with different ages each time you run it? It's a lot of work to have to change each occurrence of `17` to whatever age the user wants to use!

So your job is to edit the code provided, to use one or more variables, along with user input.

To start, use `input()` to get an integer value from the user and assign it to a variable called `age`.

Now replace every occurrence of `17` with `age`, so that the program uses the variable rather than the hardcoded number for each calculation.

When you are done, run your program by typing the following in the terminal window after the `$` prompt and pressing enter:

```
python variables.py
```

If you see any errors, it's time to debug! You may have left out something small or misspelled something.

Once you feel you've corrected any errors, execute `python variables.py` again, and repeat this process until no more errors appear.

Hopefully you should now see the prompt you've written. Enter a number and see what happens!

{% next %}

## Testing

### Correctness

Practice testing your own code by trying out different kinds of inputs. The goal is to get into the habit of testing your code not only with valid inputs, but for invalid inputs, as well as "corner cases": inputs that aren't technically invalid, but are not what you might normally expect to see as an input.

What happens if you enter a name instead of your age, when you get the prompt? As in:

```
Enter Your Age: Brian
Enter Your Age:
```

Does the program come back and ask again? It should do this because `get_int()` only accepts integers.

Or if you enter a number with a decimal point:

```
Enter Your Age: 17.5
Enter Your Age:
```

The program again comes back and reprompts.

What if you enter a negative number? At the prompt, try entering:

```
Enter Your Age: -15
```

This time you'll see your program do the calculation correctly, but how can someone be `-15` years old?

Eventually you'll see how to validate user inputs, but for now, your goal is to practice using variables, and to write code that is syntactically correct, which will compile and execute.

### How to Check Your Code

Once you've tested the program yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to always test it yourself as well!

```
check50 scienceacademy/problems/2021/7/variables
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 variables.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/variables
```




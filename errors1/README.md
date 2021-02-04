# Debugging Practice - Part 1

In this lab you will practice debugging programs!

## What is a debugging?

Programmers are humans, and humans make mistakes. You've probably already had this happen to you: you create a program that you *think* is going to work, but when you try and run it, it doesn't.

The process of finding and fixing errors in code is called **debugging**, and it's something programmers spend a lot of time doing.

Errors in programming are separated into two different varieties: **syntax errors** and **logic errors**. Let's start with the first one.

{% next %}

## Syntax errors

Sometimes, the computer just complains at you that something is wrong. You have made a typo, spelled something wrong, or just typed something that doesn't make sense to the computer.

That "complaint" is an **error message**, and learning how to read and understand these messages is an important skill for every programmer.

Take a look at the program `p1.py` on the right. It has a syntax error in it, but don't try and find it yet (even if you already see it). First, try and run the program:

```
python p1.py
```

Here's the error you saw:

```
Traceback (most recent call last):
  File "p1.py", line 2, in <module>
    print(f"Hello, {name}")
NameError: name 'name' is not defined
```

This is the format of a Python error message. Let's look at it line by line:

1. The first line, is telling you that it's going to try to show you where in your program the error occurred. In a more complex program, you might have to "trace" your way "back" to where the error happened.
1. The second line shows the name of the program file and on what line the error occurred. This is important information.
1. Third, we see the actual line of code that has the problem.
1. Finally, the last line of the message will tell you what kind of error it was ("NameError"), and a description.

So what's the problem? The last line is always the biggest clue: "name 'name' is not defined". Can you figure out what that means and why it's a problem?

{% spoiler "Hint" %}

This code is looking for a variable named `name`, but there's no such thing. In the previous line, the user's name is stored in a variable, but it's spelled `your_name`.

In line 2, change `name` to `your_name` and try running again.

{% endspoiler %}

Try "messing" up the code in other ways, like removing a `"` or a `)`, and see what happens when you run it. Notice how the error message changes.

{% next %}

## TypeError

Take a look at `p2.py` on the right. The goal of this program is to get a number and add 10 to it. Run the program:

```
python p2.py
```

Break down the error message just like we did last time. Remember to focus on the last line:

```
Traceback (most recent call last):
  File "p2.py", line 2, in <module>
    print(f"Your number plus 10 is {10 + num}")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Can you see what the error is telling you? Fix the code so that it works correctly.

{% spoiler "Hint" %}

The message is saying that the problem is with the `+` sign: having an `int` on one side and a `str` on the other side is "unsupported", meaning it's not allowed.

We need to change the right-side operand (`num`) to an integer.

{% endspoiler %}

{% next %}

## Multiple errors

What happens if you have multiple errors? Take a look at `p3.py` on the right. This program is full of errors - you may even see some of them already. Before you fix anything, though, try running it.

Did you notice that there was only one error message? It turns out that when Python finds an error, it just stops. It doesn't matter if there are more errors later in the program, the first error is what gets reported.

This means that as you repeat the cycle of finding, fixing, and testing, you'll eventually work your way through every error in the code.

Fix all of the errors in `p3.py`. Remember to keep running the program each time you change something. There are 7 things that need fixing!

{% next %}

## Logic errors

The second type of error is a bit trickier to solve. A *logic error* happens when the program works, but not as you expected. Rather than just type something the computer doesn't understand, you've told it to do something - just not what you *thought* you told it!

Click on `p4.py`. The purpose of this program is to find the product of a list of numbers. It asks for 5 numbers, then loops through the list and multiplies each number. Go ahead and run it to see the results.

Wait a minute! Did you get `0`? What's going on? Try and think about it before clicking the hint.

{% spoiler "Hint" %}

The code loops through the list of numbers, multiplying each time, but since `result` starts out as `0`, the result is `0 * 4 * 9 * 3 * 7`.

Oops! What should `result` be?

{% endspoiler %}

You may have spotted this one right away, but it's a simplified example. In a bigger program, these kinds of mistakes can be tricky to find. Since there's no error message, the computer is just happily doing what you told it to do - you just made a mistake in *logic*.

{% next %}

### How to Check Your Code

Once you've tested the program yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to always test it yourself as well!

```
check50 scienceacademy/problems/2021/7/errors1
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 p1.py
style50 p2.py
style50 p3.py
style50 p4.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/errors1
```




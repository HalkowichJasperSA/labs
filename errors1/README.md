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
  File "p1.py", line 1, in <module>
    Print("hello, world")
NameError: name 'Print' is not defined
```

This is the format of a Python error message. Let's look at it line by line:

1. The first line, is telling you that it's going to try to show you where in your program the error occurred. In a more complex program, you might have to "trace" your way "back" to where the error happened.
1. The second line shows the name of the program file and on what line the error occurred. This is important information.
1. Third, we see the actual line of code that has the problem.
1. Finally, the last line of the message will tell you what kind of error it was ("NameError"), and a description.

So what's the problem? The last line is always the biggest clue: "name 'Print' is not defined". Can you figure out what that means and why it's a problem?

{% spoiler "Hint" %}

This code is looking for a command (ie *function*) named `Print`, but there's no such thing. Computers are case-sensitive, and Python's print function is spelled `print`.

Change the `P` to a `p` and try running again.

{% endspoiler %}

Try "messing" up the code in other ways, like removing a `"` or a `)`, and see what happens when you run it. Notice how the error message changes.

{% next %}

## Logic errors

The second type of error is a bit trickier to solve. A *logic error* happens when the program works, but not as you expected. Rather than just type something the computer doesn't understand, you've told it to do something - just not what you *thought* you told it!

Take a look at `p2.py` on the right. The goal of this program is to multiply a list of numbers and print the product. Run the program:

```
python p2.py
```

Wait a minute! `4 * 9 * 3 * 7` is not `0`. What's going on? Try and think about it before clicking the hint.

{% spoiler "Hint" %}

The code loops through the list of numbers, multiplying each time, but since `product` starts out as `0`, the result is `0 * 4 * 9 * 3 * 7`.

Oops! `product` should be `1`...

{% endspoiler %}

You may have spotted this one right away, but it's a simplified example. In a bigger program, these kinds of mistakes can be tricky to find. Since there's no error message, the computer is just happily doing what you told it to do - you just made a mistake in *logic*.

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/variables
```




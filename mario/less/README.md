# Mario

## World 1-1

Toward the end of World 1-1 in Nintendo's _Super Mario Brothers_, Mario must ascend a right-aligned pyramid of blocks, as shown below.

![screenshot of Mario jumping up a right-aligned pyramid](pyramid.png)

Let's recreate that pyramid in Python, by using hashes (`#`) for bricks, a la the below. Each hash is a bit taller than it is wide (at least for the font we're using), so the pyramid itself will also appear taller than it is wide.

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

The program we'll write will be called `mario.py`. And let's allow the user to decide just how tall the pyramid should be by first prompting them for a positive integer between 1 and 8, inclusive.

Here's how the program might work if the user inputs `8` when prompted:

```
$ python mario.py
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

Here's how the program might work if the user inputs `4` when prompted:

```
$ python mario.py
Height: 4
   #
  ##
 ###
####
```

Here's how the program might work if the user inputs `2` when prompted:

```
$ python mario.py
Height: 2
 #
##
```

And here's how the program might work if the user inputs `1` when prompted:

```
$ python mario.py
Height: 1
#
```

If the user doesn't, in fact, input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:

```
$ python mario.py
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #
  ##
 ###
####
```

How to begin? Let's approach this problem one step at a time.

{% next %}

## Pseudocode

First, write in `pseudocode.txt` at right some pseudocode that implements this program, even if you're not (yet!) sure how to write it in code. There's no one right way to write pseudocode, but short English sentences suffice. Odds are your pseudocode will use (or imply using!) one or more functions, conditions, Boolean expressions, loops, and/or variables.

{% spoiler %}

There's more than one way to do this, so here's just one!

1. Prompt user for height.
1. If height is less than 1 or greater than 8 (or not an integer at all), go back to step one.
1. Count *n* from 1 through height:
    1. On iteration *n*, print *n* hashes

It's okay to edit your own after seeing this pseudocode here, but don't simply copy/paste this into your own!

{% endspoiler %}

{% next %}

## Prompting for Input

Whatever your pseudocode, let's first write only the code that prompts (and re-prompts, as needed) the user for input.

Specifically, modify `mario.py` at right in such a way that it prompts the user for the pyramid's height, storing their input in a variable as an integer, re-prompting the user again and again as needed if their input is not a positive integer between 1 and 8, inclusive. Then, just print the value of that variable, thereby confirming (for yourself) that you've indeed stored the user's input successfully, a la the below.

```
$ python mario.py
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
OK: 4
```

{% spoiler "Hints" %}

* Recall that you can print an `int` with `print()`.
* Recall that you can convert the user's input with `int()`.
* Don't forget to check for when the user enters a non-number, like "hi". Remember `try...except`?

{% endspoiler %}

## Building the Opposite

Now that your program is (hopefully!) accepting input as prescribed, it's time for another step.

It turns out it's a bit easier to build a left-aligned pyramid than right-, like this:

```
#
##
###
####
#####
######
#######
########
```

So let's build a left-aligned pyramid first and then, once that's working, right-align it instead!

Modify `mario.py` at right such that it no longer simply prints the user's input but instead prints a left-aligned pyramid of that height.

{% spoiler "Hints" %}

* Keep in mind that a hash is just a character like any other, so you can print it with `print()`.
* In Python we have a `for` loop, via which you can iterate some number times. Perhaps on each iteration, *i*, you could print that many hashes?
* When you print something, Python automatically adds a newline at the end (as if you'd hit "Enter"). If you don't want this, you can tell `print()` to use a different "end". Example `print("#", end="")` would print nothing after.
* You can actually "nest" loops, iterating with one variable (e.g., `i`) in the "outer" loop and another (e.g., `j`) in the "inner" loop. For instance, here's how you might print a square of height and width `n`, below. Of course, it's not a square that you want to print for this problem!

```
for i in range(n):
    for j in range(n):
        print("#", end="")
    print("")
```

{% endspoiler %}

{% next %}

## Right-Aligning with Dots

Now, let's right-align that pyramid by pushing its hashes to the right by prefixing them with dots (i.e., periods), a la the below.

```
.......#
......##
.....###
....####
...#####
..######
.#######
########
```

Modify `mario.py` in such a way that it does exactly that!

{% spoiler "Hint" %}

Notice how the number of dots needed on each line is the "opposite" of the number of that line's hashes. For a pyramid of height 8, like the above, the first line has just 1 hash and thus 7 dots. The bottom line, meanwhile, has 8 hashes and thus 0 dots. Via what formula (or arithmetic, really) could you print the right number of dots and hashes on each line?

{% endspoiler %}

### How to Test Your Code

Does your code work as prescribed when you input:

* `-1` (or other negative numbers)?
* `0`?
* `1` through `8`?
* `9` or other positive numbers?
* letters or words?
* no input at all, when you just hit Enter?

{% next %}

## Removing the Dots

All that remains now is a finishing flourish! Modify your program so that it prints spaces instead of those dots!

### How to Test Your Code

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

```
check50 scienceacademy/problems/2021/7/mario/less
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 mario.py
```

{% spoiler "Hint" %}

A space is just a press of your space bar, just as a period is just a press of its key! Just remember that `print()` requires that you surround both with double quotes!

{% endspoiler %}

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/mario/less
```

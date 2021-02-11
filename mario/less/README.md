# Mario

## World 1-1

Toward the end of World 1-1 in Nintendo's _Super Mario Brothers_, Mario must climb a right-aligned pyramid of blocks, as shown below.

![screenshot of Mario jumping up a right-aligned pyramid](pyramid.png)

Let's recreate that pyramid in Python, by using hashes (`#`) for bricks, like shown below. Each hash is a bit taller than it is wide (at least for the font we're using), so the pyramid itself will also appear taller than it is wide.

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

The program you'll write will be called `mario.py`. And it also should allow the user to decide just how tall the pyramid should be by first prompting them for a positive integer between 1 and 8, inclusive.

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

If the user doesn't, in fact, input a positive integer between 1 and 8, inclusive, the program should re-prompt the user until they cooperate:

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

## Step 1: Prompting for Input

Let's first write only the code that prompts (and re-prompts, as needed) the user for input.

Specifically, modify `mario.py` at right so that it prompts the user for the pyramid's height, storing their input in a variable as an integer. Make sure to re-prompt the user again and again if their input is not a positive integer between 1 and 8, inclusive. Then, just print the value of that variable to confirm (for yourself) that you've indeed stored the user's input successfully. Running the program should look like this:

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

* Recall that you can convert the user's input with `int()`.
* Don't forget to check for when the user enters a non-number, like "hi". Remember the `try...except` example we did in class?

```python
try:
    num = int(input("Pick a number: "))
except ValueError:
    print("That's not a number!")
```

{% endspoiler %}

## Step 2: Building the Opposite

Now that your program is (hopefully!) accepting input correctly, it's time for another step.

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

Modify `mario.py` at right so that it no longer prints the user's input but instead prints a left-aligned pyramid of that height.

{% spoiler "Hints" %}

* Keep in mind that a hash is just a character like any other, so you can print it with `print()`.
* You've learned about the `for` loop: maybe on each iteration, *i*, you could print that many hashes?
* When you multiply a string by an integer, you get that string repeated. For example:

```python
print("$" * 5)
```

Would print `$$$$$`. This could be very helpful to you!

{% endspoiler %}

{% next %}

## Step 3: Right-Aligning with Dots

Now, let's right-align that pyramid by pushing its hashes to the right by prefixing them with dots (i.e., periods), like this:

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

Modify `mario.py` so that it does exactly that!

{% spoiler "Hint" %}

Notice how the number of dots needed on each line is the "opposite" of the number of that line's hashes. For a pyramid of height 8, like the above, the first line has just 1 hash and 7 dots. The second line has 2 hashes and 6 dots, and so on. The bottom line has 8 hashes and 0 dots. Via what formula (or arithmetic, really) could you print the correct number of dots and hashes on each line?

{% endspoiler %}

### Test Your Code

Does your code work as required when you input:

* `-1` (or other negative numbers)?
* `0`?
* `1` through `8`?
* `9` or other positive numbers?
* letters or words?
* no input at all, when you just hit Enter?

{% next %}

## Step 4: Removing the Dots

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

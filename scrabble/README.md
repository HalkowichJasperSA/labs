# Scrabble

Determine which of two Scrabble words is worth more.

```
$ python scrabble.py
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

## Background

In the game of [Scrabble](https://scrabble.hasbro.com/en-us/rules), players create words to score points, and the number of points is the sum of the point values of each letter in the word.

|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|1|3|3|2|1|4|2|4|1|8|5|1|3|1|1|3|10|1|1|1|1|4|4|8|4|10|

For example, if we wanted to score the word `Code`, we would note that in general Scrabble rules, the `C` is worth `3` points, the `o` is worth `1` point, the `d` is worth `2` points, and the `e` is worth `1` point. Summing these, we get that `Code` is worth `3+1+2+1 = 7` points.

## Implementation Details

Finish `scrabble.py` at right, so that it finds the winner of a short scrabble-like game, where two players each enter their word, and the higher scoring player wins.

* You've been provided the point values of each letter of the alphabet in a dictionary named `POINTS`.

  * For example, `A` or `a` is worth 1 point (represented by `POINTS["a"]`), `B` or `b` is worth 3 points (represented by `POINTS["b"]`), etc.

* You have a function called `score()` that takes a string as input and returns an `int`. Whenever you want to assign point values to a particular word, you can call this function.

* The program prompts the two players for their words using the `input()` function. These values are stored inside variables named `p1` and `p2`.

* In `score()`, your program should use the `POINTS` dictionary to compute and return the score for the string argument. Characters that are not letters should be given zero points, and uppercase and lowercase letters should be given the same point values.

  * For example, `!` or `3` are worth `0` points while `A` and `a` are both worth `1` point.

* Finally, your program should print, depending on the players' scores, `"Player 1 Wins!"`, `"Player 2 Wins!"`, or `"Tie!"`.

### Hints

* You may find the string function `lower()` to be helpful.

* You can find if a character is a letter of the alphabet using `isalpha()`. For example, `"a".isalpha()` would return `True`.

* Printing out the scores is a good way to check if your program is working correctly. You can remove the `print()` statements when you're done.

### How to Test Your Code

Your program should behave as the examples below.

```
$ python scrabble.py
Player 1: Question?
Player 2: Question!
Tie!
```

```
$ python scrabble.py
Player 1: Oh,
Player 2: hai!
Player 2 wins!
```

```
$ python scrabble.py
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

```
$ python scrabble.py
Player 1: Scrabble
Player 2: wiNNeR
Player 1 wins!
```

{% next %}

## How to Test Your Code

Execute the below to evaluate the correctness of your code using `check50`. But be sure to run it yourself as well!

```
check50 scienceacademy/problems/2021/7/scrabble
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 scrabble.py
```

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted.

```
submit50 scienceacademy/problems/2021/7/scrabble
```

# Hello

## Listing Files

Hello, world! At right, in the *text editor*, is the very first program you wrote in Python, in a file called `hello.py`.

Click the folder icon, and you'll see that `hello.py` is the only file that's present at the moment. Click the folder icon again to hide all that.

Next, in the *terminal window* at right, immediately to the right of the dollar sign (`$`), otherwise known as a *prompt*, type precisely the below (in lowercase), then hit Enter:

```
ls
```

Do you see only `hello.py`? That's because you've just listed the files in that same folder, this time using a command-line interface (CLI), using your keyboard, rather than the graphical user interface (GUI) represented by that folder icon. In particular, you *executed* (i.e., ran) a command called `ls`, which is shorthand for "list." (It's such a frequently used command that its authors called it just `ls` to save keystrokes.) Make sense?

From here on out, to "execute" (i.e., run) a command means to type it into a terminal window and then hit Enter. Commands are *case-sensitive*, so be sure not to type in uppercase when you mean lowercase or vice versa.

{% next %}

## Running programs

Execute the below to run your program:

```
python hello.py
```

Phew!

## Getting User Input

Suffice it to say, no matter how you compile or execute this program, it only ever prints `hello, world`. Let's personalize it.

Modify this program in such a way that it first prompts the user for their name and then prints `hello, so-and-so`, where `so-and-so` is their actual name.

As before, execute your program, testing it a few times with different inputs, with:

```
python hello.py
```

{% spoiler "Hints" %}

#### Don't recall how to prompt the user for their name?

Recall that you can use `input()` as follows, storing its *return value* in a variable called `name` of type `string`.

```python
name = input("What is your name? ")
```

#### Don't recall how to print a variable?

Don't recall how to include the user's name with a greeting? Recall that you can use `f` to print a "format string" ("f" is for "format"), a la the below:

```python
print(f"hello, {name}")
```

{% endspoiler %}

### How to Test Your Code

Once you've tested the program yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to test it yourself as well!

```
check50 scienceacademy/problems/2020python/hello
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 hello.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2020ap/hello
```

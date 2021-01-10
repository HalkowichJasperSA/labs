# Input Practice

##

{% next %}

## Running programs

Execute the below to run your program:

```
python hello.py
```

Success!

## Getting User Input

No matter how many times you execute this program, it only ever prints `hello, world`. Let's personalize it.

Modify this program in such a way that it first prompts the user for their name and then prints `hello, so-and-so`, where `so-and-so` is their actual name.

As before, execute your program, testing it a few times with different inputs, with:

```
python hello.py
```

{% spoiler "Hints" %}

#### Don't recall how to prompt the user for their name?

Recall that you can use `input()` as follows, storing its *return value* in a variable called `name`.

```python
name = input("What is your name? ")
```

#### Don't recall how to print a variable?

Don't recall how to include the user's name with a greeting? You can use `f` to print a "format string" ("f" is for "format") like this:

```python
print(f"hello, {name}")
```

{% endspoiler %}

### How to Test Your Code

Once you've tested the program yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to test it yourself as well!

```
check50 scienceacademy/problems/2021/7/hello
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 hello.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/hello
```

# Lists and Strings

In this lab you will learn:

- What is a list
- How to create and use arrays
- Why a `for` loop is so useful for lists and strings

## What is a list?

A **list** is a type of data structure in Python that can hold multiple values in one variable. There are many reasons you may want to do this. Say, for instance, you want to get the average grade for a class of 30 students. You can create 30 variables, add them up and divide by 30:

```python
student1 = 95
student2 = 84
student3 = 93
...
```

You can see pretty quickly that it's going to get very boring typing in so much repetitive code!

{% next %}

Instead, you can use a list, named `students` that can store many values:

```python
students = []
```

The square brackets `[]` indicate a list. Right now it's empty, but we can fill it up using a loop.

You can add values to `students` by using `append()` - **append** means "add on to the end". Since you've already assigned the list, you just need a loop to ask for the 30 grades:

```python
for i in range(30):
    grade = float(input("Enter a grade: "))
    students.append(grade)
```

At the end of this loop, `students` will have 30 grades in it!

{% next %}

Lists can store many pieces of information, but individual pieces can also still be used.

An item's position in the list is called its **index**. Lists are **zero-indexed**, meaning the first item in the list always has an index of zero.

For example, imagine you have the following list:

```python
colors = ["red", "green", "blue", "orange"]
```

`"red"` would be at index `0`, `"blue"` at index `2`, and so on. You can access an individual item from a list using its index:

```python
print(colors[1])  # This would print "green"

colors[3] = "purple"  # This would change the last item to "purple"
```

Since the index is a number, and you can find how long a list is with `len()`, you could loop through every item in the list like this:

```python
for i in range(len(colors)):
    print(colors[i])
```

This is called **iterating** through a list.

However, in Python, there's a much easier way to loop through a list. You can get the same result with:

```python
for item in colors:
    print(item)
```

As you can see, rather than using the index and counting your way through, you can loop through the items in the list directly.

{% next %}

## Strings

Recall in the "data types" lab you learned about the **string** type.

```python
name = "Wanda"
```

In Python, strings can be used in many of the same ways as lists:

```python
len(name)  # Finds how long the name is.

# This prints each letter in the name one at a time.
for char in name:
    print(char)

print(char[3])  # This prints "d"
```

However, one difference is that strings are **immutable**, which means they can't be altered. While you can assign a value to a list index, you can't do it with a string:

```python
name = "Wanda"
colors = ["red", "green", "blue", "orange"]

colors[2] = "pink"  # This is OK
name[4] = "o"  # This will produce an error
```

{% next %}

## Your Turn!

To the right are two programs you will complete.

In `list.py`, write a `for` loop that iterates through the `numbers` list and changes each number to its square, then prints the result.

```
$ python list.py
[4, 49, 16, 25, 81]
```

{% spoiler "Hint" %}
Remember that you can loop through a list's indices like this:

```python
# change every item in the list to a 0
for i in range(len(numbers)):
    some_list[i] = 0
```

{% endspoiler %}

{% next %}

In `string.py`, you need to take the given name and count how many vowels occur in the name. Print the number (just the number, nothing extra).

Example of running the program:

```
$python string.py
Enter your name: Luigi
3
```

{% spoiler "Hint" %}

* Remember the "forloop" lab, where you added the numbers from one to 10. You'll need to do something very similar here to count how many vowels you see.

* Remember that you can loop through a string one letter at a time using:

```python
for char in name:
    print(char)
```

{% endspoiler %}

{% next %}

### How to Check Your Code

Once you've tested the programs yourself, execute the below to evaluate the correctness of your code using `check50`. But be sure to always test it yourself as well!

```
check50 scienceacademy/problems/2021/7/lists
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 lists.py
```

and

```
style50 string.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 scienceacademy/problems/2021/7/lists
```

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

Instead, you can use a list, named `students` that can store many values:

```python
students = []
```

The square brackets `[]` indicate a list. Right now it's empty, but we can fill it up using a loop.

{% next %}

You can add values to `students` by using `append()` - **append** means "add on to the end". Since you've already assigned the list, you just need a loop to ask for the 30 grades:

```python
for i in range(30):
    grade = float(input("Enter a grade: "))
    students.append(grade)
```

At the end of this loop, `students` will have 30 grades in it!

{% next %}

Individual

Lists are **zero-indexed**, meaning the first item in the list always has an index of zero.

This is called **iterating** through a list.

{% next %}

## Strings

Arrays in C can store values of any data type, as long as all elements in the array are of the same type. In fact, a **string** in C is really an array of `chars`.

When we declare a string in C as in:

```c
string course = "CS50";
```

we are creating an array named `course` with one character at each index. There is one additional character at the end of every string in C: the null-terminator, represented by `'\0'`. The null-terminator is the character that tells a string that the string is over, and that there are no more characters in the string. So this array will have five spots for chars, indexed 0 through 4.

We can index into this string in the same way we index into any array, using square bracket notation. So `course[0]` has a value of `'C'`, `course[1]` a value of `'S'`, ending with `course[4]` having a value of `'\0'`. Even though `'\0'` looks like two characters, our program see it as one `char`.

Since a string is an array, we can iterate through a string using a for loop as well. There is a special function `strlen()` we can use which gives us the length of a string. To use this function, we need to write `#include <string.h>` at the top of our program to access the `string.h` library.

Our for loop to access each character of our string, one `char` at a time would look like:

```c
for (int i = 0; i < strlen(course); i++)
{
    printf("%c\n", course[i]);
}
```

Here we print out each letter stored in the string variable `course` on its own line.

{% next %}

## Your Turn!

To the right are two programs you will complete. First, you'll modify `string.c` to include a for loop that iterates through the string `name` and print out one character per line.

Then complete the program `array.c` which creates a new integer array named `hours`, in which you will input the number of hours you spent on homework each day for the last 5 days, and then print out the hours for each day. Your output should look like:

```
Day 1: <day 1 hours>
Day 2: <day 2 hours>
```

and so on, where `<day 1 hours>` is replaced with the number you input for day 1.

{% spoiler "Hint" %}
You can use a for loop like this to prompt for the number of hours for each of the 5 days:

```c
for (int i = 0; i < NUM_DAYS; i++)
{
    // prompt for hours using `get_int()` and store the result in `hours[i]`
}
```

Then use the same for loop a second time to iterate through these values and print them. Inside this second loop you will have something like:

```c
printf("Day %i: %i", i + 1, hours[i]);
```

Why do you think we're printing the value `i + 1` for the day?

{% endspoiler %}

Make sure to compile and test both programs!

[Download our CS50 Reference sheet on Arrays and Strings](https://cs50.harvard.edu/ap/2020/assets/pdfs/arrays_and_strings.pdf)

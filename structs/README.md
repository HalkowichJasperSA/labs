# Structures and encapsulation

In this lab you will learn:

- What structs are and why we use them
- How to create and use structs

## What is a struct?

There are times that you want to store data that is related, but of different data types, in one variable. This bundling of data is called **encapsulation**. In other programming languages, you might do this with an **object**, but in C, there's something more basic: the **data structure** or just **struct**.

Say you want to keep track of a class of 25 students, and each student has a name, a student id number, a year, and a gpa. Until now, the only way you could do this would be to create four arrays, one for each of these types of data. You'd have to declare all four arrays, each with a size of *25*, and make sure to keep them in sync, so that the same index in each refers to the same student. What a hassle!

Instead, you can group this data together in one variable using a **struct**. You can create a new data type named `student`, which has four **members**, `string name`, `int id`, `int year` and `float gpa`. Conveniently, you can set up this structure without having to declare how *many* students there will be.

To summarize, using **structs** you can create your own data types, which will prove useful as you deal with more complex programming problems!

{% next %}

## How to define and use structs

You create a new struct as follows:

```c
typedef struct
{
    string name;
    int id;
    int year;
    float gpa;
}
student;
```

This defines a new data type called `student`. You then can create a new `student` variable in the same way you declare a new `int`: by typing the data type followed by the new variable name:

```c
student s;
```

You can then set each member (or *property*) of the variable `s`, by typing:

```c
s.name = "Alice";
s.id = 12345;
s.year = 2020;
s.gpa = 4.0;
```

If you want to keep track of *25* students, you can declare an array named `students` with a data type of `student`:

```c
student students[25];
```

You access each `student` in the `students` array in the usual way with `[i]`, and use the `.name` syntax to access particular elements within the struct. To access the name of the first student in the `student` array: `students[0].name`.

{% next %}

## Your Turn

Your job is to complete the program, `mystruct.c`, and create your own datatype, add data to a few members, and then print them out. You do not need to define your structure in a header file.

The basic definition of a new data type is already there, just change the name of your new structure from `name_goes_here` to something of your choosing.

You may declare either a single variable or an array using your new data type. If you use an array, you'll want to use a `for` loop to add and print the data for each member.

Be sure to test your code with valid data, invalid data, and corner cases!

[Download the CS50 Reference sheet on Structures and Encapsulation](https://cs50.harvard.edu/ap/2020/assets/pdfs/structures_and_encapsulation.pdf)

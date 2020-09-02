# Terminal

![Terminal](https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/terminal/command_line_practice.gif)

In this lab you will learn:

- How to use a command-line interface
- Terminal commands to navigate through your workspace
- Creating folders and files using the command-line
- Moving and renaming files

## What is the terminal?

On the bottom of your window on the right is a **terminal** panel, which is a text-based or **command-line** interface to your workspace. The command line is a powerful tool to explore your workspace's files and directories, compile code, run programs, and even install software.

{% next %}

## Exploring your workspace

Before we start, you may notice three text files open in the code/text editor on the upper right side of your screen. These files are located somewhere in your workspace, but they may not stored in the appropriate directories. We'll take a closer look at these later.

Under the tab that says `>_ Terminal`, is a window with a `$` prompt. This is the terminal window where you can type commands.

Let's start by exploring your workspace. Your workspace contains *folders*, aka *directories* (the terms are interchangeable) and files. Directories can be nested inside other directories, just as you might have folders stored in other folders on your computer.

## The `ls` and `cd` terminal commands

Let's see what files are in the directory you're currently located in (your current *working directory*). Type `ls` at the `$` (`ls` is short for **list**). This lists all the files (including directories) in your current directory.

When you use `ls`, you'll see only the files in your working directory. You can't see or access files inside other directories.

You should see `apt1/` in blue. The `/` indicates that `apt1` is a directory. We can see what's inside of `apt1` by making it the working directory. Type this:

```
cd apt1
```

at the prompt (`cd` is short for **change directory**). If you type `ls` again, you will see the files contained in `apt1`.

{% next %}

The output of this second `ls` should be `kitchen/   living_room/`. Now type:

```
cd living_room
```

to change your working directory to `living_room` and look at what's inside with `ls`.

You'll see `fridge/`, which is a directory, and `living_room_contents.txt` in white, meaning it's a regular file. In fact, this is one of the files you have open in the text editor above.

But shouldn't `fridge` be in the kitchen? Let's `cd` into `fridge` and see what is there.

You'll find one file there: `fridge_contents.txt`, which is also open in the text editor. Indeed, looking at its contents, these seem like items that should be in the kitchen, not in the living room.

Let's fix that by moving the directory `fridge` from `living_room` to `kitchen`. We'll want to do this by first positioning ourselves in the `apt1` directory. To see the entire path of our current directory (in other words, where we currently are) you can type the command `pwd` (short for **print working directory**).

You'll see that you're located in `/root/sandbox/apt1/living_room`. This is the entire path from the root (or *top* directory) of your workspace. To get to `apt1/` you need to go up one level. To do this, type:

```
cd ..
```

The two dots mean "go up one directory level". If you type in `pwd` again you'll now see you're in `/root/sandbox/apt1`.

{% next %}

## The `mv` Command

Now that you're in `apt1/`, you can now move the `fridge/` by typing:

```
mv living_room/fridge kitchen/
```

There are three parts to this statement. the `mv` stands for **move**, `living_room/fridge` identifies the `fridge` directory inside the `living_room` directory, and `kitchen/` is the `kitchen` directory. All together, this tells the computer to move the directory `fridge`, along with its contents, from the `livingroom` to the `kitchen`.

The `fridge_contents` file may disappear from the text editor section on top of your screen, but it's not deleted. You can see a graphical representation of the directory structure by clicking on the folder symbol to the left of the tabs, opening the "Directory Sidebar". You can then click on each of these directories to see exactly what is inside. The `fridge` with its `fridge_contents.txt` should now be where it belongs in the `kitchen`.

**Note:** The `mv` command is used both to **move** a file as well as to **rename** a file.

{% next %}

## Making a New Directory with `mkdir`

Let's add a few new rooms to our apartment! First make sure you are positioned in the `apt1/` directory. Check this with either `pwd` or `ls`.

You can use the command `mkdir` which means **make directory**. It will make a new directory inside your working directory. Type:

```
mkdir bedroom
mkdir bathroom
```

Now type `ls` to see what's in `apt1/`. You'll see the two new directories show up along with the two previously existing ones. Your apartment now has four rooms!

{% next %}

## Go Ahead Now and Experiment

Now it's your turn to practice the terminal commands you just learned. Try using the `cd` and `ls` commands as you navigate through the directories in your workspace. Create a few new files and directories and then move these files from one directory to another.

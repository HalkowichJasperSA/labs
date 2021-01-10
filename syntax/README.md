# Syntax

![SyntaxVideo](https://raw.githubusercontent.com/cs50nestm/cs50labs/2019/syntax/syntax.gif)

In this lab you will learn:

- What syntax is
- When to use parentheses and double quotes
- When and why to use indentation
- The syntax needed to create a program in Python

## What is Syntax?

In linguistics, *syntax* is the set of rules for using words, phrases, and punctuation to form sentences. As you can see above, if the word order of a sentence is incorrect, you might not understand what is being said to you.

{% next %}

## Syntax in Python

In computer science, **syntax** is also important for a computer to understand what you are telling it to do. Each programming language has its own syntactical rules, which include the combination of both words and punctuation.

For instance, to say "hello" in Python, we would write:

```python
print("hello,  world")
```

Note that the `print` function takes an **argument**, or parameter, which is wrapped in symmetrical parentheses: `(` and `)`. Parentheses *always* come in pairs - every left one must have a matching right!

You may also notice the double quotes `"`, which are also symmetrical, and which surround words or sequences of characters. We call these sequences of characters `strings`.

{% next %}

## Now it's Your Turn!

Now it's your turn to try out decoding some syntax in C!

Take a look at the program on the right. There are several syntactical errors in it. See if you can edit the code to correct the errors. Look carefully at all the details in the example above for reference.

When you are done, **compile** your program by typing the following in the terminal window after the `$` prompt followed by Enter.

```
make syntax
```

If you see any errors, it's time to debug! You may have left out something small like a `;` or misspelled something. If you have a hard time finding your error, try "prepending" `help50` to your command like this:

```
help50 make syntax
```

Once you feel you've corrected any errors, execute `make syntax` again, and repeat this process until no more errors appear.

Then execute your program, by typing in the following, again followed with `enter`:

```
./syntax
```

<style type="text/css">
#green {color:green;}
</style>

### Styling with `style50`

Though C doesn't care about how you style your code (in other words code with correct syntax but inconsistent spacing will compile and execute), CS50 does! That's because spacing your code consistently makes it easier to read and as we'll see soon, easier to debug.

You can check that your spacing is correct by executing the following at the `$` prompt:

```
style50 syntax.c
```

If there’s room for improvement in your code’s style, highlighted in red will be any characters you should delete, and highlighted in green will be any characters you should add.

When style50 outputs:

<div id="green">
    <pre><code>Looks good!</code></pre>
</div>

you are done! Congratulations, you've completed the Syntax Lab!

[For more info, download the CS50 Syntax Reference Sheet](https://cs50.harvard.edu/ap/2020/assets/pdfs/syntax.pdf)

# Hexadecimal

In this lab you will learn about:

- What hexadecimal is
- Why it is useful

## What is hexadecimal?

Earlier this year you learned about number systems; specifically about the **binary** number system, which is how computers store data. Binary systems (which use base *2*) store all data as *0*s and *1*s. We contrasted this to our everyday **decimal** number system (base *10*) which uses ten digits, `0-9`. **Hexadecimal** is a numbering system which uses 16 symbols. In addition to the symbols `0-9`, it uses `a`, `b`, `c`, `d`, `e`, and `f`, for the additional digits (corresponding to `10`, `11`, `12`, `13`, `14`, and `15` in decimal.

In the same way that decimal numbers have place values that are powers of ten, and binary numbers use place values that are powers of two, hexadecimal numbers have place values that are powers of sixteen. So the hexadecimal number `0x13BA` would equate to 16<sup>0</sup> x A (A is the symbol for 10) plus 16<sup>1</sup> x B (or 11) plus 16<sup>2</sup> x 3 plus 16<sup>3</sup> x 1 which is `10 + 176 + 768 + 4096` for a total of *5050*.

{% spoiler "What's this `0x` thing?" %}

When you're working with different bases, it can be unclear what value a particular number has. For example, if you see `110`, does that mean *110* in decimal, *6* in binary, or *272* in hexadecimal? For this reason, numbers in bases *other* than decimal use a **prefix** to identify them.

Hexadecimal numbers are identified by `0x`, so we'd write `0x110` to be clear that we mean *272*. Binary is written with `0b`, so `0b110` clearly means *6*.

{% endspoiler %}

{% next %}

## Why is hexadecimal useful?

It turns out that binary numbers get very large very quickly. To express the decimal number 15, for instance, we need four place values in binary: `1111`. To express the number *5050* above (`0x13BA`), we'd need 13 places: `1001110111010`.

Note that there's a relationship: *4* digits of binary represent values from 0-15, and *1* digit of hexadecimal represents the same range. For this reason, computer scientists settled on hexadecimal as a more convenient way to represent those larger numbers.

### Representing bytes

Here's another handy example: Remember that *8* bits represent one **byte**? We can write those values, which range from 0-255, with just two digits of hexadecimal. It's much more convenient to write `0xff` than `0b11111111`.

{% next %}

## Representing colors

Colors in a computer typically represented in red, green, and blue values (RGB), each in the range of `0-255`, or one byte. In many applications, such as web design, "hex" color codes are written in the format `#rrggbb` where the `rr` is the hex value of red, `gg` for green, and `bb` for blue. So for instance `#000000` represents black since each color is displayed at their lowest possible intensity, and `#FFFFFF` represents mixing each of the three primary colors at their full intensity which gives us white.

> Capitalization doesn't really have a meaning in hexadecimal, so you'll often see it written in both forms. Most languages allow both, so programmers just pick one and stick with it. What's your preference?

{% next %}

## Your turn

Complete the second `for` loop in the program on the right to convert a hexadecimal number to a decimal (base 10) number.

After prompting the user for a hexadecimal number, the program iterates through the string and uses a function `isxdigit()` which checks that each character is a legal hexadecimal digit. The same loop then changes all digits to upper case, so that you can use the same algorithm to convert `'a'` or `'A'` to the `int` `10`.

{% spoiler "Hint" %}

1. Remember that the hexadecimal value is stored in a `string`, so that characters that appear as numbers, 0-9, are actually ASCII `char`s. The `char` `'0'` has an ASCII value of *48*. Can you come up with an algorithm to convert the `char` `'0'` to the `int` `0`?
2. What about the a-f `char`s in the hexadecimal number? Since the ASCII value of `'A'` has numeric value of *65*, and a hexadecimal `'A'` is *10* in decimal, can you add or subtract something from `'A'` to get an result of *10*?


{% endspoiler %}

[Download our CS50 Reference sheet on Hexadecimal](https://cs50.harvard.edu/ap/2020/assets/pdfs/hexadecimal.pdf)

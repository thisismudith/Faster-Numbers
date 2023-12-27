# Faster Numbers

Have you ever thought of a different way to write numbers? Base Number Systems are fun and intriguing, however, imagine a number system that's based upon positioning as per distinct permutations. Sounds confusing? Let's look at an example:

## **Base Number System:** (Original)
**Base: 10** *(Conventional)*\n
Number: 240 = (2 × 10²) + (4 × 10¹) + (0 × 10⁰) = 240\n
**Base: 26**\n
Number: 240 = (2 × 26²) + (4 × 26¹) + (0 × 26⁰) = 1456

## **Permutation Position Number System:** (New -- Used in the code)
Works as per the principles of permutations. Let's look at an example:

Suppose we use `REF = abcdefghijklmnopqrstuvwxyz`.  With this, we can write:
`a = 1, b = 2, ... , z = 26, aa = 27, ... , zz = 702, ...`
This trend can also be observed in the naming and numbering of excel columns:
| Column Name | Column Number |
| :---:   | :---: |
| A | 1  |
| Z | 26  |
| AA | 27  |
| AAA | 703  |
| AAZ | 728  |
| XYZ | 16900  |

Continuing this pattern, we can observe:
- A total of 26 numbers can be written using 1 character (i.e. a = 1 ; z = 26)
- A total of 702 numbers can be written using 2 characters (i.e a = 1 ; aa = 27 ; zz = 702)
- A total of 18,278 numbers can be written using 3 characters
...
- A total of 146,813,779,479,510 numbers can be written using 10 characters.
.. and so on

## **Why Faster Numbers?**

This number system is memory efficient as the number of bits required to store the same data decreases significantly. Here are a few statistics:
Number: `int('9' * 10000)` *# The number 9 repeated 10000 times* (10,000 digits)

##### **Faster Numbers:**
REF: ```abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ``` *(REF or reference is the string characters used to permute the numbers)*
Memory (before): `10 kb`
Memory (after): `5 kb`
Memory Efficiency: `50%`
Converting Time (execution): `15.625 ms`

##### **Factors Affecting Memory Efficiency:**
-  ∝ Total Digits *(i.e. as total number of digits will increase, memory efficiency will increase)*
-  ∝ REF string length *(i.e as REF string length will increase, memory efficiency will increase)*

## Installation

```sh
git clone https://github.com/thisismudith/Faster-Numbers/
cd Faster-Numbers
```

## Usage

##### Constants:
- `REF`: The *reference* characters used from the string to permute numbers. [CUSTOMIZABLE]
- `START`: The first numerical value that shall be assigned. *(i.e. in a = 1, START = 1)* [CUSTOMIZABLE]

##### Functions:
- `lengthPossibilities()`
- `charToNum()`
- `numToChar()`
*Detailed description given within the functions*

##### Faster Numbers in Action:
**Code:**
```py
# sys.set_int_max_str_digits(9999)  # Use this to allow bigger digits
REF = ascii_lowercase  # The reference string
START = 1
char = "thisismudith"
num = 42069

print("REF:", REF)
print("BASE:", BASE)
print("Minimum Number Possible:", START)
print(f"Maximum Number Possible by Char Length of {len(char)}: {lengthPossiblity(len(char), START)}")
print("Char → Num:", charToNum(char, START))
print("Num → Char:", numToChar(num,  START))
```
**Output:**
```sh
>>> REF: abcdefghijklmnopqrstuvwxyz
>>> BASE: 26
>>> Minimum Number Possible: 1
>>> Maximum Number Possible by Char Length of 12: 99246114928149462
>>> Char → Num: 74589138072142884
>>> Num → Char: bjfa
```

## License

[MIT](https://github.com/thisismudith/Faster-Numbers/blob/main/LICENSE)

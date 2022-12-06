# Strings Quiz

**NOTE:** 
- The functions for questions 6 and 7 can be executed in [CodeSkulptor3/Strings_Quiz](https://py3.codeskulptor.org/#user307_MYVcul3A4d_2.py)

- The functions for the Practice Exercises for Strings can be executed in [CodeSkulptor3/Practice_Exercises](https://py3.codeskulptor.org/#user307_My0kRGcvLI_1.py)


## Questions


1. Which of the expressions below select the last character in the string **"Grail"**? 

**Answer:**

- "Grail"[-1]
- "Grail"[4]

2. Which of the string slices below selects the string **"Anthrax"** from the string **"Castle Anthrax"**?

**Answer:**

- "Castle Anthrax"[7  :]
- "Castle Anthrax"[7  : 15]

3. Which one of the operators below can not be used with strings in Python?

**Answer:** - (subtraction)

4. What does the expression **a_str.find(sub)** do when the string **sub** is not a substring 
of the string **a_str**?

**Answer:** Return the value -1

5. Which of the string format expressions below return the string "abracadabra"?

**Answer:**

```{python}
"{2}{1}{0}".format("abra", "cad", "abra")
"{0}{1}{0}".format("abra", "cad")
```

6. Write a function **count_vowels(word)** that takes the string **word** as input and returns 
the number of occurrences of lowercase vowels (i.e. the lowercase letters **"aeiou"**) in **word**. 
**Hint:** Python has a built-in string method that can count the number of occurrences of a letter in a string.

After you have implemented **count_vowels**, run the following two statements:

```{python}
print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
```

The first statement should print 13 in the console. Enter the second number printed in the 
console in the box below.

**Answer:** 17

```{python}
def count_vowels(str):
    """
    Take a string word as input and returns the number of 
    occurrences of lowercase vowels
    """
    vowels = str.count('a') + str.count('e') + str.count('i') + str.count('o') + str.count('u')
    return vowels

print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
```

        13
        17

7. Write a function **demystify(l1_string)** that takes a string composed of the characters **"l"** and **"1"** and returns the string formed by replacing each instance of **"l"** by **"a"** and each instance of **"1"** by **"b"**.

Once you have implemented demystify, test your function with calls below.

```{python}
print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
```

The first call should print the string "aaabbbabababbbbaaa" in the console. 
Enter the second string printed in the console in the text box below. Do not include 
enclosing quotes.

**Answer:** bbbababbabbaaabaaabaaabbbbbaabbabaababbb

```{python}
def demystify(l1_string):
    """
    Take a string composed of the characters "l"
    and "1" and returns the string formed by replacing each 
    instance of "l" by "a" and each instance of "1" by "b".
    """
    first = l1_string.replace("l", "a")
    second = first.replace("1", "b")
    return second

print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
```

        aaabbbabababbbbaaa
        bbbababbabbaaabaaabaaabbbbbaabbabaababbb
# Dictionaries Quiz

**NOTE:** 
- The function to question 7 can be executed in [CodeSkulptor3/Dictionaries_Quiz](https://py3.codeskulptor.org/#user307_K8KeBlDtGG_2.py)

- The functions for the Practice Exercises for Dictionaries can be executed in [CodeSkulptor3/Practice_Exercises](https://py3.codeskulptor.org/#user307_blOIbNEmnl_0.py)

## Questions

1. Which of the following expressions corresponds to a dictionary with no elements?

**Answer:**

- `dic()`
- `{}`

2. Given an existing dictionary **favorites**, what Python statement adds the key **"fruit"** to this dictionary with the corresponding value **"blackberry"**?

**Answer:**

```{python}
favorites["fruit"] = "blackberry"
```

3. Which of the expressions below returns True when the dictionary my_dictionary contains the key my_key and False otherwise?

**Answer:**

```{python}
my_key in my_dictionary
```

4. Keys in a dictionary can have which of the following types?

**Answer:**

- float
- tuple

5. Values in a dictionary can have which of the following types?

**Answer:**

- tuple
- dict
- bool
- string

6. Consider the following dictionary:

```{python}
instructor_ratings = {"Joe" : "awesome", "Scott" : "hmmm..."}
```

What happens when Python evaluates the expression **instructor_ratings["John"]**?

**Answer:**

Since "John" is not a key in the dictionary, Python raises a KeyError exception.

7. Write a function **count_letters(word_list)** that takes as input a list of words that are composed entirely of lower case letters . This function should return the lower case letter that appears most frequently (total number of occurrences) in the words in **word_list**. (In the case of ties, return the earliest letter in alphabetical order.)

The Python code snippet below represents a start at implementing **count_letters** using a dictionary **letter_count** whose keys are the lower case letters and whose values are the corresponding number of occurrences of each letter in the strings in **word_list**.

```{python}
def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
        
    # enter code here
```

Complete your implementation of **count_letters** based on this snippet.  As a test, **count_letters(["hello", "world"])** should return the letter **’l’** since **’l’** appears 3 times total in the strings **"hello"** and **"world"**.

When you are confident in your code, compute the lower case letter return by **count_letters(monty_words)** where **monty_words** is defined as shown.

```{python}
monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")
```

Enter this single letter in the text box below. Do not include any spaces or enclosing quotes around the letter.

**Answer: e**

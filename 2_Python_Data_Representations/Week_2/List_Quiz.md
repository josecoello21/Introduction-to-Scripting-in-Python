# Lists Quiz

**NOTE:** 
- The function to question 7 can be executed in [CodeSkulptor3/Lists_Quiz](https://py3.codeskulptor.org/#user307_iv4DqvXRCc_1.py)

- The functions for the Practice Exercises for Lists can be executed in [CodeSkulptor3/Practice_Exercises](https://py3.codeskulptor.org/#user307_TAZrpYx3EG_0.py)


## Questions


1. Which of the following expressions  evaluates to the list [0,  1, 2, 3, 4, 5]?

**Answer:**

- `list(range(6))`
- `list(range(0, 6))`

2. Let my_list be the list ["This", "course", "is", "great"].

- What is len(my_list)?

- What non-negative number is the index of "great"? I.e., how would you replace the question marks in my_list[???] so that the resulting value is "great"?

Submit two numbers, one for each of these two questions, separated by spaces.

**Answer:** 4 3

3. If we want to split a list my_list into two halves, which of the following uses slices to do so correctly?

More precisely, if the length of my_list is 2n, i.e., even, then the two parts should each have length n. If its length is 2n+1, i.e., odd, then the two parts should have lengths n and n+1.

**Answer:**

- **my_list[0 : len(my_list) // 2]** and **my_list[len(my_list) // 2 : len(my_list)]**
- **my_list[: len(my_list) // 2]** and **my_list[len(my_list) // 2 :]**

4. If nn and mm are non-negative integers, consider the list final_list computed by the code snippet below.

```{python}
init_list = list(range(1, n))
final_list = init_list * m
```

The length of this list depends on the particular values of nn and mm used in computation. Which option below correctly expresses the length of final_list in terms of nn and mm?

**Answer:** `(n−1) × m`

5. If nn is a non-negative integer, consider the list split_list computed by the code snippet below.

```{python}
test_string = "xxx" + " " * n + "xxx"
split_list = test_string.split(" ")
```

The length of this list depends on the particular values of nn used in computation. Which option below correctly expresses the length of split_list in terms of n?

**Answer:** *n + 1*

6. Select the code snippets below in which list2 is a copy of list list1 (as opposed to simply being another reference to the list list1).

**Answer:**

```{python}
list1 = list(range(1, 10))
list2 = [] + list1
```

```{python}
list1 = list(range(1, 10))
list2 = list(list1)
```

```{python}
list1 = list(range(1, 10))
list2 = list1[:]
```

7. Write a function **strange_sum(numbers)** that takes a list of integers and returns the sum of those items in the list that are not divisible by 33.  When you are done, test your function using the code snippet below.

```{python}
print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
```

The first line in the test should print the number **24** in the console. Enter the second number printed in the console in the box below.

```{python}
def strange_sum(my_int_list, my_sum = 0, idx = 0):
    if idx == len(my_int_list)-1:
        if (my_int_list[idx] % 3) != 0:
            return my_sum + my_int_list[idx]
        else:
            return my_sum
        
    if (my_int_list[idx] % 3) != 0:
        my_sum += my_int_list[idx]
    
    idx += 1

    return strange_sum(my_int_list, my_sum = my_sum, idx = idx)

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
```

        24
        6994
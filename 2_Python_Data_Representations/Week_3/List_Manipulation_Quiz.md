# List Manipulation Quiz

**NOTE:** 
- The functions for questions 6 and 7 can be executed in [CodeSkulptor3/Lists_Manipulation_Quiz](https://py3.codeskulptor.org/#user307_IjLwwQO5ZB_5.py)

- The functions for Practice Exercises for List Manipulation can be executed in [CodeSkulptor3/Practice_Exercises](https://py3.codeskulptor.org/#user307_thIVtN28sg_1.py)

## Questions

1. Given the list my_list = [1, 3, 5, 7, 9], which of the following slices returns the list [3, 5, 7, 9]?

**Answer:** my_list[ 1 : ]

2. While of the following expressions returns a tuple of length one?

**Answer:**

- (1, )
- ((1, ))

3. Why does following code snippet raise an error in Python?

```{python}
instructors = ("Scott", "Joe", "John", "Stephen")
instructors[2 : 4] = []
print(instructors)
```
**Answer:** Tuples are immutable.

4. Given a non-empty list my_list, which item in the list does the operation my_list.pop() remove?

**Answer:** The item **my_list[-1]**

5. What output does the following code snippet print to the console?

```{python}
my_list = [1, 3, 5, 7, 9]
my_list.reverse()
print(my_list.reverse())
```
Note that this question is easily answered by running this snippet in Python. Instead, **carefully** evaluate this code snippet mentally when you attempt this problem.

**Answer:** None

6. Given a list fib = [0, 1], write a loop that appends the sum of the last two items in fib to the end of fib.  What is the value of the last item in fib after twenty iterations of this loop?  Enter the answer below as an integer.

As a check, the value of the last item in fib after ten iterations is 89.

```{python}
def fib(my_list, n):
    if n <= 0:
        return my_list
    else:
        n_th = sum(my_list[len(my_list)-2:])
        my_list.append(n_th)
        return fib(my_list, n-1)
        
print(fib([0,1], 20)[-1])
```

        10946

**Answer:** 10946

7. One of the first examples of an algorithm was the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes/). This algorithm computes all prime numbers up to a specified bound.  The provided code below implements all but the innermost loop for this algorithm in Python. Review the linked Wikipedia page and complete this code.

```{python}
"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        # Remove appropriate multiples of divisor from answer
        pass
    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))
```

Running your completed code should print two numbers in the console. The first number should be 46. 
Enter the second number printed in the console as the answer below.

```{python}
def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    answer = [2,3,5,7]
    for divisor in range(11, bound, 2):
        # Remove appropriate multiples of divisor from answer
        count = 0
        for i in answer:
            if (divisor % i) == 0:
                count += 1
                break
        if count == 0:
            answer.append(divisor)
    return answer

print(len(compute_primes(2000)))
```

        303
        
**Answer:** 303
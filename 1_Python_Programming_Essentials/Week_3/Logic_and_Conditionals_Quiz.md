# Logic and Conditionals Quiz

**NOTE:** The function to question 7 can be executed in [CodeSkulptor3/Logic_Conditionals_Quiz](https://py3.codeskulptor.org/#user307_vJxZR1LbRg_3.py)

1.  Which of the following are Boolean values in Python?

**Answer:** `False`, `True`

2.  Consider the Boolean expression not (p or not q). Give the four following values in order, separated only by spaces:

the value of the expression when p is `True`, and q is `True`,

the value of the expression when p is `True`, and q is `False`,

the value of the expression when p is `False`, and q is `True`,

the value of the expression when p is `False`, and q is `False`,

Remember, each of the four results you provide should be `True` or `False` with the proper capitalization.

**Answer:** `False False True False`

3.  Given the following initialization:

```{python}
bool1 = True
bool2 = False
```

Which of the expressions below evaluate to `True`?

**Answer:**

-   not False
-   bool1 != False
-   not (bool1 == bool2)

4.  Two expressions are *logically equivalent* if they have the same value for all possible values of the variables that comprise the expression.

Given two numbers num1 and num2, which one of the expressions below is logically equivalent to the following arithmetic comparison:

```{python}
num1 >= num2
```

**Answer:**

```{python}
(num1 > num2) or (num1 == num2)
```

5.  An if statement can have how many else parts?

**Answer:** 1

6.  In Python, conditional statements may be nested. Consider the following function that takes two Boolean values as input and returns a Boolean value.

```{python}
def nand(bool1, bool2):
    """
    Take two Boolean values bool1 and bool2
    and return the specified Boolean values
    """
    
    if bool1:
        if bool2:
            return False
        else:
            return True
    else:
        return True
```

Which Boolean expression below is logically equivalent to the function call `nand(bool1, bool2)` where bool1 and bool2 are Boolean variables?

**Answer:** `not (bool1 and bool2)`

7.  The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture#Statement_of_the_problem) is an example of a simple computational process whose behavior is so unpredictable that the world's best mathematicians still don't understand it.

Consider the simple function $f\left ( n \right )$ (as defined in the Wikipedia page above) that takes an integer *n* and divides it by two if *n* is even and multiplies *n* by 3 and then adds one to the result if *n* is odd. The conjecture involves studying the value of expressions of the form $f\left ( f\left ( f\left ( ...f\left ( f\left ( n \right ) \right ) \right ) \right ) \right )$ as the number of calls to the function *f* increases. The conjecture is that, for any non-negative integer *n*, repeated application of *f* to *n* yields a sequence of integers that always includes 1.

Your task for this question is to implement the Collatz function *f* The key to your implementation is to build a test that determines whether *n* is even or odd by checking whether the remainder when *n* is divided by 2 is either zero or one. **Hint:** You can compute this remainder in Python using the remainder opertor `%` via the expression `n % 2`. Note you will also need to use integer division `//` when computing *f*.

Once you have implemented *f* test the your implementation on the expression *f(f(f(f(f(f(f(674)))))))*. This expression should evaluate to 190. Finally, compute the value of the expression *f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))* and enter the result below as an integer. Remember to use copy and paste when moving the expressions above into your Python environment. Never try to retype expressions by hand.

```{python}
def collatz_function(n = None, nested = 1):
    
    if not isinstance(n and nested, int):
        return print('parameters must be integers') 
    
    if n and nested < 0:
        return print('parameters must be greater than zero')
    
    if nested == 1 and (n % 2) == 0:
        return n//2
    elif nested == 1:
        return 3*n + 1
    else:
        return collatz_function(n = collatz_function(n = n, nested = 1), nested = nested - 1)

    
print(collatz_function(n = 674, nested = 7))
print(collatz_function(n = 1071, nested = 14))
```

    190
    3053

**Answer:** 3053
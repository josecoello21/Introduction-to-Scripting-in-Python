# Functions Quiz

**NOTE:** The functions for questions 5, 6 and 7 can be executed in [CodeSkulptor3/Functions_Quiz](https://py3.codeskulptor.org/#user307_0omLBDPsMg_4.py)

1.  Consider the following Python function definition:

```{python}
def cube_root(val):
    """
    Given number, return the cube root of the number
    """
    return val ** (1 / 3)
```

**Answer:** cube_root(1.0)

2.  Running the following program results in the error:

`SyntaxError: bad input on line 5 (’return’)`

Which of the following describes the problem?

```{python}
def max_of_2(val1, val2):
    if val1 > val2:
        return val1
    else:
    return val2

def max_of_3(val1, val2, val3):
    return max_of_2(val1, max_of_2(val2, val3))
```

**Answer:** Incorrect indentation.

3.  The following code has a number of syntactic errors in it. The intended math calculations are correct, so the only errors are syntactic. Fix these errors.

Once the code has been fully corrected, it should print out two numbers. The first should be 1.09888451159. Submit the second number printed in [CodeSkulptor3](http://py3.codeskulptor.org/). Make sure that you enter at least four digits after the decimal point.

```{python}
define project_to_distance(point_x point_y distance):
    dist_to_origin = (pointx ** 2 + pointy ** 2) ** 0.5
     scale == distance / dist_to_origin
    print point_x * scale, point_y * scale

project-to-distance(2, 7, 4)
```

**Answer:**

```{python}
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)
```

    1.098884511589512 3.846095790563293

**3.846095790563293**

4.  A common error for beginning programmers is to confuse the behavior of `print` statements and `return` statements.

-   `print` statements can appear anywhere in your program and print a specified value(s) in the console. Note that execution of your Python program continues onward to the following statement. Remember that executing a `print` statement inside a function definition does not return a value from the function.

-   `return` statements appear inside functions. The value associated with the `return` statement is substituted for the expression that called the function. Note that executing a `return` statement terminates execution of the function definition immediately. Any statements in the function definition following the `return` statement are ignored. Execution of your Python code resumes with the execution of the statement after the function call.

As an example to illustrate these points, consider the following piece of code:

```{python}
def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())
```

    Hello world
    Is it over yet?

Note that this code calls the function `do_stuff` in the last print statement. The definition of `do_stuff` includes two `print` statements and one `return` statement.

Which of the following is the console output that results from executing this piece of code? While it is trivial to solve this question by cutting and pasting this code into CodeSkulptor, we suggest that you first attempt this question by attempting to execute this code in your mind.

**Answer:**

    Hello world
    Is it over yet?

5.  Implement the mathematical function $f\left ( x \right ) = -5x^{5} + 67x^{2} - 47$ as a Python function. Then use Python to compute the function values $f\left ( 0 \right )$, $f\left ( 1 \right )$, $f\left ( 2 \right )$ and $f\left ( 3 \right )$. Enter the maximum (largest) of these four values calculated below.

A common error for this question is to fail to read the directions above carefully and submit your answer in the incorrect form. As a coder, always remember to note exactly what answers your code (and quiz questions) should produce.

```{python}
def my_function(x):
    my_result = -5*(x**5) + 67*(x**2) - 47
    return my_result

my_args = (0,1,2,3)

maxi, count, results = None, 1, []

for i in my_args:
    if count == 1:
        maxi = my_function(x = i)
    elif my_function(x = i) > maxi:
        maxi = my_function(x = i)
    
    count += 1
    
    results.append(my_function(x = i))
    
    
    
print('my results are: ', results)
print(' ')
print('My maximum is: ', maxi)
```

    my results are:  [-47, 15, 61, -659]

    My maximum is:  61

**Answer:** 61

6.  When investing money, an important concept to know is compound interest. The equation $FV = PV\left ( 1 + rate \right )^{periods}$ relates the following four quantities.

-   The present value *(PV)* of your money is how much money you have now.

-   The future value *(FV)* of your money is how much money you will have in the future.

-   The nominal interest rate per period *(rate)* is how much interest you earn during a particular length of time, **before** accounting for compounding. This is typically expressed as a percentage.

-   *The number of periods (periods)* is how many periods in the future this calculation is for.

Finish the following code, run it, and submit the printed number. Provide at least four digits of precision after the decimal point.

```{python}
def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    

print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))
```

Before submitting your answer, test your function on the following example. `future_value(500, .04, 10, 10)` should return 745.317442824

**Hint:** If you are stuck on this question, try working problem 7 of the Practice Exercises for Functions.

**Answer:**

```{python}
def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    fv = present_value * (1 + rate_per_period)**periods
    return fv
    

print("$1000 at 2% compounded daily for 4 years yields $",future_value(500, .04, 10, 10))
print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))
```

    $1000 at 2% compounded daily for 4 years yields $ 745.3174428239327
    $1000 at 2% compounded daily for 4 years yields $ 1083.284693436586

**1083.284693436586**

7.  For this final question, your task is to find the formula for a simple geometric problem using Google and then implement that formula in Python. While you may think that it is silly that we don't just give you the formula, scripting in Python often requires one to do a substantial amount of searching for information. This question requires you to practice this important task.

Write a Python function that computes the area of an equilateral triangle given the length of one of its sides. Search for a mathematical formula that specifies this relation and translate that formula into Python. **Hint:** The desired formula involves taking a square root. Remember that you compute a square root of a number in Python by raising that number to the 0.5 power using the \*\* operator.

As a test, your area function should return an area of 1.73205080757 for an equilateral triangle with sides of length 2. Now, use this function to compute the area of equilateral triangle with sides of length 5. Enter this area as a number (and not the units) with at least four digits of precision after the decimal point.

**Answer:**

```{python}
def my_triangle(a = None):
    my_area = (1/4) * 3**(1/2) * a**2
    return my_area

print(my_triangle(a = 5))
```

    10.82531754730548

**10.82531754730548**

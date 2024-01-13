### Input Size and Efficiency
1. As the input to an algorithm increases, the time required to run the algorithm may also increase
    - Complexity **n** function (by counting the number of output lines printed)
    - This type of relationship is called a **linear** relationship
        ```python
        def say_hello(n):
            for i in range(n):
                print("Hello!")
        ```

<br><br> 

2. As the input to an algorithm increases, the time required to run the algorithm may also increase—**and different algorithms may increase at different rates.** 
    - Complexity **n<sup>2</sup>** function (by counting the number of output lines printed)
    - This is what we would call a **quadratic** rate of increase.
        ```python
        def say_hello(n):
            for i in range(n):
                for i in range(n):
                    print("Hello!")
        ```

<br><br> 

- We've looked here only at a couple of different rates—linear and quadratic. But there are many other possibilities. Here we'll show some of the common types of rates that come up when designing algorithms:

    <p align="center">
    <img style="height:300px; width:300px" alt="Graph showing linear and quadratic relationships." src="https://video.udacity-data.com/topher/2019/March/5c92f7e6_00-all-comparison-computational-complexity/00-all-comparison-computational-complexity.svg"><br>
    
    <span>Derivative of <a target="_blank" href="https://commons.wikimedia.org/wikiFile:Comparison_computational_complexity.svg">"Comparison of computational complexity"</a> by <a target="_blank" href="https://commons.wikimedia.org/wiki/User:Cmglee">Cmglee</a>. Used under <a target="_blank" href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">CC BY-SA 4.0</a>.</span>
    </p>

- We should note that when people refer to the rate of increase of an algorithm, they will sometimes instead use the term order. Or to put that another way:
    - The *rate of increase* of an algorithm is also referred to as the **order** of the algorithm.

    For example, instead of saying "this relationship has a linear rate of increase", we could instead say, "the *order* of this relationship is linear".<br>

    On the section, we'll introduce something called ***Big O Notation***, and you'll see that the "**O**" in the name refers to the **o**rder of the rate of increase.

<br>


### Big-O Notation
The "O" in the name refers to the *order* of the function or algorithm in question. And that makes sense, because big O notation is used to describe the order—or rate of increase—in the run-time of an algorithm, in terms of the input size (`n`). <br>
- **n** represents the length of the input to your algoritm. To get the "O" value of a function, count the number of times each line is implemented. e.g consider the pseudo-code for a decoding string function that accepts any length of input
    ```bash
    function decode(input):
        create output string                  # Line 1 is performed only once
        for each letter in input:             # Lines 3-4 are performed every n-times
            get new_letter from letters location in cipher
            add new_letter to output
        return output                         # Line 5 is performed only once
    ```

    The Big O notation can be described as **`O(2n + 2)`**. <br>
    Suppose the input string is "jzqh". Then `n = 4`

In the example we've looked at here, we've been approximating efficiency by counting the number of lines of code that get executed. But when we are thinking about the run-time of a program, what we really care about is how fast the computer's processor is, and how many operations we're asking the processor to perform. Different lines of code may demand very different numbers of operations from the computer's processor. For now, counting lines will work OK as an approximation, but as we go through the course you'll see that there's a lot more going on under the surface.

<br>

### Worst Case and Approximation
Suppose that we analyze an algorithm and decide that it has the following relationship between the input size, `n`, and the number of operations needed to carry out the algorithm:

<p>N = n<sup>2</sup> + 5</p>

Where `n` is the input size and N is the number of operations required.

For example, if we gave this algorithm an input of 2, the number of required operations would be 2<sup>2</sup> + 5 or simply 9. <br>

The thing to notice in the above exercise, is this: In N = n<sup>2</sup> + 5, the 
5 has very little impact on the total efficiency—especially as the input size gets larger and larger. Asking the computer to do 10,005 operations vs. 10,000 operations makes little difference. Thus, it is the <b>n<sup>2</sup></b> that we really care about the most, and the `+5` makes little difference. <br>

Most of the time, when analyzing the efficiency of an algorithm, the most important thing to know is the order. In other words, we care a lot whether the algorithm's time-complexity has a linear order or a quadratic order (or some other order). This means that very often (in fact, most of the time) when you are asked to analyze an algorithm, you can do so by making an approximation that significantly simplifies things. <br>

For large values of **n** e.g. <b>4n<sup>2</sup> + 3n + 7</b> the other terms become irrelevant in their size and therefore can be discarded.

<br>


### Space Complexity
When we refer to space complexity, we are talking about how efficient our algorithm is in terms of memory usage. This comes down to the datatypes of the variables we are using and their allocated space requirements. In Python, it's less clear how to do this due to the underlying data structures using more memory for house keeping functions (as the language is actually written in C). <br>

For example, in C/C++, an integer type takes up 4 bytes of memory to store the value, but in Python 3 an integer takes 14 bytes of space. Again, this extra space is used for housekeeping functions in the Python language. <br>

For the examples of this lesson we will avoid this complexity and assume the following sizes: <br>
<table>
    <thead>
        <tr >
            <th>Type</th><th>Storage size</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>char</td> <td>1 byte</td>
        </tr>
        <tr>
            <td>bool</td> <td>1 byte</td>
        </tr>
        <tr>
            <td>int</td> <td>4 bytes</td>
        </tr>
        <tr>
            <td>float</td> <td>4 bytes</td>
        </tr>
        <tr>
            <td>double</td> <td>8 bytes</td>
        </tr>
    </tbody>
</table>

It is also important to note that we will be focusing on just the data space being used and not any of the environment or instructional space. <br>

**Example 1**
```python
def our_constant_function():

    x = 3 # Type int
    y = 345 # Type int
    z = 11 # Type int

    answer = x+y+z

    return answer
```
So in this example we have four integers (`x`, `y`, `z` and `answer`) and therefore our space complexity will be `4*4 = 16 bytes`. This is an example of **constant space complexity**, since the amount of space used does not change with input size. <br>

**Example 2**
```python
def our_linear_function(n):
    
    n = n # Type int
    counter = 0 # Type int
    list_ = [] # Assume that the list is empty (i.e., ignore the fact that there is actually meta data stored with Python lists)

    while counter < n:
        list_.append(counter)
        counter = counter + 1
    
    return list_
```
So in this example we have two integers (`n` and `counter`) and an expanding list, and therefore our space complexity will be `4*n + 8` since we have an expanding integer list and two integer data types. This is an example of **linear space complexity**.




### Resources
- [Big-O Cheatsheet](https://www.bigocheatsheet.com/)
- [Python Complexities](https://wiki.python.org/moin/TimeComplexity)
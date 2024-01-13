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
<img style="height:300px; width:300px" alt="Graph showing linear and quadratic relationships." src="https://video.udacity-data.com/topher/2019/March/5c9120f9_02-n-squared-comparison-computational-complexity/02-n-squared-comparison-computational-complexity.svg"><br>
<span>Derivative of <a target="_blank" href="https://commons.wikimedia.org/wikiFile:Comparison_computational_complexity.svg">"Comparison of computational complexity"</a> by <a target="_blank" href="https://commons.wikimedia.org/wiki/User:Cmglee">Cmglee</a>. Used under <a target="_blank" href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">CC BY-SA 4.0</a>.</span>
</p>


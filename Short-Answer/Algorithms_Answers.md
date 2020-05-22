#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
While there is multiplication of n in this problem, O(x(n)) is simplified down to O(n). That means the loop that takes n into account has the biggest effect on runtime. 


b) O(n) 
While there is a nested loop in this algorithm, it does not depend on the input. That means the answer is O(n).


c) O(n)
This is a recursive function that takes in n.

## Exercise II

The input would be a sorted list of numbers representing floors. 

To solve this, I would start in the middle of the list, then drop an egg off that floor. 
If it breaks, I would split the lower half of the list in half and drop the egg from there. 
If it does not break, I would split the upper half of the list in half and drop the egg from there. 

I would do this until I find the 2 neighboring floors where one is "not broken" and the next one is "broken". 

That is the highest the egg will be able to go without breaking. 

The runtime complexity of this algorithm would be O(logn) because of how it splits things in half over and over to find the solution. 

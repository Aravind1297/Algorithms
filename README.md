# Algorithms/ Knapsack problem

Task--> The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

Input Format--> The first line of the input contains the number π of items and the capacity π of a knapsack.
The next π lines define the values and weights of the items. The π-th line contains integers π£π and π€πβthe
value and the weight of π-th item, respectively.

Constraints--> 1 β€ π β€ 10E3, 0 β€ π β€ 2 Β· 10E6; 0 β€ π£π β€ 2 Β· 10E6, 0 < π€π β€ 2 Β· 10E6 for all 1 β€ π β€ π. All the
numbers are integers.

Output Format--> Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most
10β3. To ensure this, output your answer with at least four digits after the decimal point.

Since this is a Maximization Problem, Greedy Algorithm is used to solve this problem.


Efficient Greedy Algorithm for Knapsack problem:

  1. Sort items by decreasing value/weight 
  2. if first item fits into knapsack, take all of it and move to next item.
  3. otherwise take so much as to fill the knapsack
  4. Return total value and amounts taken.
  
  
Mathemetical Implementation:


Assume v1/w1 >= v2/w2 >= ..... >= vn/wn


knapsack(π,w1,v1,w2,v2,....wn,vn):

  A <---[0,0,...0] , v <-- 0
  for i from 1 to n:
    if π = 0:
      return (V,A)
      
     a <--- min(wi,π)
     v <--- v + a * vi/wi
     wi <--- wi - a, A[i] <-- A[i] +  a, W <-- W - a
  return (v,A)
  
  
Analysis:

* Each iteration is O(1)
* knapsack after sorting is O(n)
* sort + knapsack is O(nlogn)


Note: For simplicity, I have sorted the weight value pair in the main script and declared it to the knapsack function parameter. 




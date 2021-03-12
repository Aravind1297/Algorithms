# Algorithms/ Knapsack problem

Task--> The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

Input Format--> The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
value and the weight of 𝑖-th item, respectively.

Constraints--> 1 ≤ 𝑛 ≤ 10E3, 0 ≤ 𝑊 ≤ 2 · 10E6; 0 ≤ 𝑣𝑖 ≤ 2 · 10E6, 0 < 𝑤𝑖 ≤ 2 · 10E6 for all 1 ≤ 𝑖 ≤ 𝑛. All the
numbers are integers.

Output Format--> Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most
10−3. To ensure this, output your answer with at least four digits after the decimal point.

Since this is a Maximization Problem, Greedy Algorithm is used to solve this problem.


Efficient Greedy Algorithm for Knapsack problem:

  1. Sort items by decreasing value/weight 
  2. if first item fits into knapsack, take all of it and move to next item.
  3. otherwise take so much as to fill the knapsack
  4. Return total value and amounts taken.
  
  
Mathemetical Implementation:


Assume v1/w1 >= v2/w2 >= ..... >= vn/wn


knapsack(𝑊,w1,v1,w2,v2,....wn,vn):

  A <---[0,0,...0] , v <-- 0
  for i from 1 to n:
    if 𝑊 = 0:
      return (V,A)
      
     a <--- min(wi,𝑊)
     v <--- v + a * vi/wi
     wi <--- wi - a, A[i] <-- A[i] +  a, W <-- W - a
  return (v,A)
  
  
Analysis:

* Each iteration is O(1)
* knapsack after sorting is O(n)
* sort + knapsack is O(nlogn)


Note: For simplicity, I have sorted the weight value pair in the main script and declared it to the knapsack function parameter. 




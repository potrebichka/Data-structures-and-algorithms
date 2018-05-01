## 1. Maximum Pairwise Product Problem
* Find the maximum product of two distinct numbers in a sequence of non-negative 
integers.*

**Input:** A sequence of non-negative integers.
**Output:** The maximum value that can be obtained by multiplying two different

## 2-1. Fibonacci number
*Given an integer n, find the nth Fibonacci number Fn.*

**Input:** A single integer n.

**Output:** Fibonacci number Fn.

## 2-2. Last digit of a large Fibonacci number
*Find the last digit on the nth Fibonacci number.*

**Input:** A single integer n (0<=n<=10^7).

**Output:** The last digit of Fn.


## 2-3. Greatest commot divisor
*Find the greatest common divisor of two integers.*

**Input:** Two integers a and b (1<=a,b<=2*10^9).

**Output:** Greatest common divisor.

## 2-4. Least Common Multiple
*Find the least common multiple of two integers.*

**Input:** Two integers a and b (1<=a,b<=2*10^9).

**Output:** The least common multiple of a and b.

## 2-5. Huge Fibonacci number
*Find Fibonacci number Fn modulo m.*

**Input:** Two integers n (1<=n<=10^18) and m (2<=m<=10^5).

**Output:** Fn mod m.

## 2-6. Last digit of the sum of Fibonacci numbers
*Find the last digit of a sum of the first n Fibonacci numbers.*

**Input:** A single integer n (0<=n<=10^14).

**Output:** Last digit of F0+F1+...+Fn.

## 2-7. Last digit of the sum of Fibonacci numbers again
*Find the last digit of a partial sum of Fibonacci numbers Fm+Fm+1+...+Fn.*

**Input:** Two integers m and n (0<=m,n<=10^18).

**Output:** The last digit of Fm + Fm+1 + ... + Fn.

## 3-1. Money change.
*Find the minimum number of coins needed to change the input value into coins with 
denominations 1, 5, 10.*

**Input:** A single integer m (1<=m<=10^3).

**Output:** The minimum number of coins with denominations 1,5,10 that changes m.

## 3-2. Maximum value of the loot.
*Implement algorithm for the fractional knapsack problem.*

**Input:** The first line of the input contains the number n of items and the capacity W of a 
knapsack. The next n lines define the values and weights of the items. The i-th line contains 
integers v_i and w_i — the value and the weight of i-th item, respectively.

**Output:** The maximal value of fractions of items that fit into the knapsack.

## 3-3. Maximum advertisement revenue.
*Given two sequences a_1,a_2...a_n (a_i is the profit per click of the i-th ad) and 
b_1,b_2..b_n (b_i is the average number of clicks per day of the i-th slot), we need to 
partition them into
n pairs (a_i,b_j) such that the sum of their product is maximized.*

**Input:** The first line contains an integer n, the second one contains a sequence of 
integers a_1,a_2...a_n, the third one contains a sequence of integers b_1,b_2...b_n.

**Output:** The maximum value of \sum_{i=1}^{n} a_i*c_i.

## 3-4. Collecting signatures.
*Given a set of n segments {[a_0, b_0], [a_1, b_1], . . . , [a_n−1, b_n−1]} with integer 
coordinates on a line, find the minimum number m of points such that each segment contains at 
least one point. That is, find a set of integers X of the minimum size such that for any 
segment [a_i, b_i] there is a point x E X such that a_i ≤ x ≤ b_i.*

**Input:** The first line of the input contains the number n of segments. Each of the 
following n lines contains two integers a_i and b_i (separated by a space) defining the 
coordinates of endpoints of the i-th segment.

**Output:** Output the minimum number m of points on the first line and the integer 
coordinates of m points (separated by spaces) on the second line. You can output the points in 
any order. If there are many such sets of points, you can output any set.

## 3-5. Maximum number of prizes.
*You are organizing a funny competition for children. As a prize fund you have n candies. 
You would like to use these candies for top k places in a competition with a natural 
restriction that a higher place gets a larger number of candies. To make as many children 
happy as possible, you are going to find the largest value of k for which it is possible.*

**Input:** A single integer n.

**Output:** In the first line, output the maximum number k such that n can be represented as 
a sum of k pairwise distinct positive integers. In the second line, output k pairwise 
distinct positive integers that sum up to n (if there are many such representations, output 
any of them).

## 3-6. Maximum salary.
*As the last question of a successful interview, your boss gives you a few pieces of 
paper with numbers on it and asks you to compose a largest number from these numbers. The 
resulting number is going to be your salary, so you are very much interested in maximizing
this number.*
 
**Input:** The first line of the input contains an integer n. The second line contains 
integers a_1, a_2, . . . , a_n.

**Output:** The largest number that can be composed out of a_1, a_2,...a_n.

## 4-1. Binary search.
*Implement binary search algorithm.*

**Input:** The first line of the input contains an integer n and a sequence a_0 < a_1 < . . . 
< a_n−1 of n pairwise distinct positive integers in increasing order. The next line contains 
an integer k and k positive integers b_0, b_1, . . . , b_n−1.

**Output:** For all i from 0 to k-1, output an index 0<=j<=n-1 such that a_j=b_i or -1 if 
there is no such index.

## 4-2. Majority element.
*Check whether an input sequence contains a majority element.*

**Input:** The first line contains an integer n, the next one contains a sequence of n non-negative
integers a_0, a_1, . . . , a_n−1.

**Output**: Output 1 if the sequence contains an element that appears strictly more than n/2 
times, and 0 otherwise.

## 4-3. Improving Quick Sort.
*Redesign a given implementation of the randomized quick sort algorithm so that it works 
fast even on sequences containing many equal elements.New partition procedure  should 
partition the array into three parts: <x part, =x part, >part.*

**Input:** The first line of the input contains an integer n. The next line contains a 
sequence of n integers a_0, a_1, . . . , a_n−1.

**Output:** Sequence sorted in non-decreasing order.

## 4-4. Number of inversions.
*An inversion of a sequence a_0, a_1, . . . , a_n−1 is a pair of indices 0 ≤ i < j < n 
such that a_i > a_j . The number of inversions of a sequence in some sense measures how
close the sequence is to being sorted. For example, a sorted (in non-descending order) 
sequence contains no inversions at all, while in a sequence sorted in descending order any 
two elements constitute an inversion (for a total of n(n − 1)/2 inversions).*

**Input:** The first line of the input contains an integer n. The next line contains a
sequence of n integers a_0, a_1, . . . , a_n−1.

**Output:** Number of inversions in the sequence.

## 4-5. Organizing a Lottery.
*Given a set of points on a line and a set of segments on a line. The goal is to compute, 
for each point, the number of segments that contain this point.*

**Input:** The first line contains two non-negative integers s and p defining the number of 
segments and the number of points on a line, respectively. The next s lines contain two 
integers a_i, b_i defining the i-th segment [a_i, b_i]. The next line contains p integers 
defining points x_1, x_2, . . . , x_p.

**Output:** P non-negative integers k_0, k_1, . . . , k_p−1 where k_i is the number of 
segments which contain x_i. More formally, k_i = |{j : a_j ≤ x_i ≤ b_j}| .

## 4-6. Closest points.
*Given n points on a plane, find the smallest distance between a pair of two (different) 
points.*

**Input:** The first line contains the number n of points. Each of the following n lines 
defines a point (x_i, y_i).

**Output:** The minimum distance.

## 5-1. Money Change Again.
*A natural greedy strategy for the change problem does not work correctly for any set of
denominations. For example, if the available denominations are 1, 3, and 4, the greedy 
algorithm will change 6 cents using three coins (4 + 1 + 1) while it can be changed using 
just two coins (3 + 3). Goal now is to apply dynamic programming for solving the Money Change 
Problem for denominations 1, 3, and 4.*

**Input:** Integer money.

**Output:** The minimum number of coins with denominations 1, 3, 4 that changes money.

## 5-2. Primitive calculator.
*Given a primitive calculator that can perform the following three operations with the current 
number x: multiply x by 2, multiply x by 3, or add 1 to x. Goal is given a positive integer 
n, find the minimum number of operations needed to obtain the number n starting from the 
number 1.*

**Input:** Single integer 1<=n<=10^6.

**Output:** In the first line, output the minimum number 𝑘 of operations needed to get n from 
1. In the second line output a sequence of intermediate numbers. That is, the second line should 
contain positive integers a_0, a_2, . . . , a_k−1 such that a_0 = 1, a_k−1 = n and for all 
0 ≤ i < k − 1, a_i+1 is equal to either a_i+1, 2a_i, or 3a_i. If there are many such 
sequences, output any one of them.

## 5-3. Edit distance.
*Implement the algorithm for computing the edit distance between two strings. 
The edit distance between two strings is the minimum number of operations 
(insertions, deletions, and substitutions of symbols) to transform one string 
into another.*

**Input:** Each of the two lines of the input contains a string consisting of 
lower case latin letters.

**Output:** The edit distance between the given two strings.

## 5-4. Placing parentheses.
*Find the maximum value of an arithmetic expression by specifying the order of 
applying its arithmetic operations using additional parentheses.*

**Input:**  A string s of length 2n + 1 for some n, with symbols s_0, s_1, . . 
., s_2n. Each symbol at an even position of s is a digit (that is, an integer 
from 0 to 9) while each symbol at an odd position is one of three operations 
from {+,-,*}.

**Output:**  Maximum value of expression

## 5-5. Longest common subsequence if three sequences.
*Compute the length of a longest common subsequence of three sequences. Given 
three sequences A = (a_1, a_2, . . . , a_n), B = (b_1, b_2, . . . , b_m) and 
C = (c_1, c_2, . . . , c_l), find the length of their longest common 
subsequence, i.e., the largest non-negative integer p such that there
exist indices 1 ≤ i_1 < i_2 < · · · <= i_p ≤ n, 1 ≤ j_1 < j_2 < · · · < j_p 
≤ m, 1 ≤ k_1 < k_2 < · · · < k_p ≤ l such that a_i1 = b_j1 = c_k1 , . . . , 
a_ip = b_jp = c_kp.*

**Input:** First line: n. Second line: a_1, a_2, . . . , a_n. Third line: m. 
Fourth line: b_1, b_2, . . . , b_m. Fifth line: l. Sixth line: c_1, c_2, . . . 
, c_l.

**Output:** p


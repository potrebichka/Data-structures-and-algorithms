## 1-1. Check brackets in the code.
*Implement a feature for a text editor to find errors in the usage of brackets in the
code.*

**Input:** One string S.

**Output:** If the code in 𝑆 uses brackets correctly, output “Success" (without the 
quotes). Otherwise, output the 1-based index of the first unmatched closing bracket, and 
if there are no unmatched closing brackets, output the 1-based index of the first 
unmatched opening bracket.

## 1-2. Compute tree height.
* You are given a description of a rooted tree. Your task is to compute and output its 
height. Recall that the height of a (rooted) tree is the maximum depth of a node, or the 
maximum distance from a leaf to the root. You are given an arbitrary tree, not necessarily 
a binary tree.*

**Input:** The first line contains the number of nodes n. The second line contains n 
integer numbers from −1 to n−1 — parents of nodes. If the i-th one of them (0 ≤ 
i ≤ n−1) is −1, node i is the root, otherwise it’s 0-based index of the parent of i-th node. It is 
guaranteed that there is exactly one root. It is guaranteed that the input represents a 
tree.

**Output:** The height of the tree.

## 1-3. Network packet processing simulation.
*Implement a program to simulate the processing of network packets.*

**Input:** The first line of the input contains the size S of the buffer and the number n 
of incoming network packets. Each of the next n lines contains two numbers. i-th line 
contains the time of arrival A_i and the processing time P_i (both in milliseconds) of the 
i-th packet. It is guaranteed that the sequence of arrival times is non-decreasing 
(however, it can contain the exact same times of arrival in milliseconds — in this case 
the packet which is earlier in the input is considered to have arrived earlier).

**Output:** For each packet output either the moment of time (in milliseconds) when the 
processor began processing it or −1 if the packet was dropped (output the answers for the 
packets in the same order as the packets are given in the input). 

## 2-1. Convert array into heap 
*In this problem you will convert an array of integers into a heap. 
This is the crucial step of the sorting algorithm called HeapSort. It 
has guaranteed worst-case running time of (n log n) as opposed to 
QuickSort’s average running time of O(n log n).*

**Input:** The first line of the input contains single integer n. The 
next line contains n space-separated integers a_i.

**Output:** The first line of the output should contain single integer 
m - the total number of swaps. m must satisfy conditions 0 ≤ m ≤ 4n. 
The next m lines should contain the swap operations used to convert the 
array a into a heap. Each swap is described by a pair of integers i,j — 
the 0-based indices of the elements to be swapped. After applying all 
the swaps in the specified order the array must become a heap, that is, 
for each i where 0 ≤ i ≤ n − 1 the following conditions must be true:
1. If 2i + 1 ≤ n − 1, then a_i < a_2i+1.
2. If 2i + 2 ≤ n − 1, then a_i < a_2i+2.

## 2-2. Parallel processing
*You have a program which is parallelized and uses n independent 
threads to process the given list of m jobs. Threads take jobs in the 
order they are given in the input. If there is a free thread, it 
immediately takes the next job from the list. If a thread has started 
processing a job, it doesn’t interrupt or stop until it finishes 
processing the job. If several threads try to take jobs from the list
simultaneously, the thread with smaller index takes the job. For each 
job you know exactly how long will it take any thread to process this 
job, and this time is the same for all the threads. You need to
determine for each job which thread will process it and when will it 
start processing.*

**Input:** The first line of the input contains integers n and m. The 
second line contains m integers t_i — the times in seconds it takes any 
thread to process i-th job. The times are given in the same order as 
they are in the list from which threads take jobs. Threads are indexed 
starting from 0.

**Output:** Output exactly m lines. i-th line (0-based index is used) 
should contain two space-separated integers — the 0-based index of the 
thread which will process the i-th job and the time in seconds when it 
will start processing that job.

## 2-3. Merging tables
*Goal is to simulate a sequence of merge operations with tables in a 
database.*

**Input:** The first line of the input contains two integers n and m — 
the number of tables in the database and the number of merge queries to 
perform, respectively. The second line of the input contains n 
integers r_i — the number of rows in the i-th table. Then follow m lines 
describing merge queries. Each of them contains two integers 
destination_i and source_i — the numbers of the tables to merge.

**Output:** For each query print a line containing a single integer — 
the maximum of the sizes of all tables (in terms of the number of rows) 
after the corresponding operation.

## 3.1 Phone book.
*In this task your goal is to implement a simple phone book manager. It should 
be able to process the following types of user’s queries: add number name, del 
number, find number.*

**Input:** A single integer N in the first line — the number of queries. It’s 
followed by N lines, each of them contains one query in the format described 
above.

**Output:** Print the result of each find query — the name corresponding to the 
phone number or “not found" (without quotes) if there is no person in the phone 
book with such phone number. Output one result per line in the same order as 
the find queries are given in the input.

#3-2. Hasing with chains.
*Implement a hash table with lists chaining. You already given the number of 
buckets m and the hash function. Your program should support the following kinds 
of queries: add S, del S, find S, check i.*

**Input:** There is a single integer m in the first line — the number of 
buckets you should have. The next line contains the number of queries N. It’s 
followed by N lines, each of them contains one query in the format described 
above.

**Output:** Print the result of each of the find and check queries, one result 
per line, in the same order as these queries are given in the input.

## 4-1. Binary tree traversals.
*You are given a rooted binary tree. Build and output its in-order, pre-order 
and post-order traversals.*

**Input:** The first line contains the number of vertices n. The vertices of 
the tree are numbered from 0 to n−1. Vertex 0 is the root.
The next n lines contain information about vertices 0, 1, ..., n−1 in order. 
Each of these lines contains three integers key_i, left_i and right_i — key_i 
is the key of the i-th vertex, left_i is the index of the left child of the 
i-th vertex, and right_i is the index of the right child of the i-th vertex. 
If i doesn’t have left or right child (or both), the corresponding left_i or 
right_i or both) will be equal to −1.

**Output:** Print three lines. The first line should contain the keys of the 
vertices in the in-order traversal of the tree. The second line should contain 
the keys of the vertices in the pre-order traversal of the tree. The third line 
should contain the keys of the vertices in the post-order traversal of the 
tree.

## 4-2. Is it a binary search tree?
*You need to test whether it is a correct binary search tree.*

**Input:** The first line contains the number of vertices n. The vertices of 
the tree are numbered from 0 to n−1. Vertex 0 is the root. The next n lines 
contain information about vertices 0, 1, ..., n−1 in order. Each of these lines 
contains three integers key_i, left_i and right_i - key_i is the key of the 
i-th vertex, left_i is the index of the left child of the i-th vertex, and 
right_i is the index of the right child of the i-th vertex. If i doesn’t have  
left or right child (or both), the corresponding left_i or right_i (or both) 
will be equal to −1.

**Output:** . If the given binary tree is a correct binary search tree (see the 
definition in the problem description), output one word “CORRECT” (without 
quotes). Otherwise, output one word “INCORRECT” (without quotes).

## 4-3. Is it binary search tree? Hard version.
*To solve the same problem as the previous one, but for a more general case,
when binary search tree may contain equal keys.*

**Input:** The first line contains the number of vertices n. The vertices of 
the tree are numbered from 0 to n−1. Vertex 0 is the root. The next n lines 
contain information about vertices 0, 1, ..., n−1 in order. Each of these lines 
contains three integers key_i, left_i and right_i - key_i is the key of the  
i-th vertex, left_i is the index of the left child of the i-th vertex, and 
right_i is the index of the right child of the i-th vertex. If i doesn’t have 
left or right child (or both), the corresponding left_i or right_i (or both) 
will be equal to −1.

**Output:** If the given binary tree is a correct binary search tree (see the 
definition in the problem description), output one word “CORRECT” (without 
quotes). Otherwise, output one word “INCORRECT” (without quotes).

## 4-4. Set with range sums.
*Implement a data structure to store a set of integers and quickly compute range 
sums.*

**Input:** Initially the set S is empty. The first line contains n — the 
number of operations. The next n lines contain operations. Each operation is one 
of the following:
∙ “+ i" — which means add some integer (not i, see below) to S,
∙ “- i" — which means del some integer (not i, see below) from S,
∙ “? i" — which means find some integer (not i, see below) in S,
∙ “s l r" — which means compute the sum of all elements of 𝑆 within some range 
of values (not from l to r, see below).
However, to make sure that your solution can work in an online fashion, each 
request will actually depend on the result of the last sum request. Denote M = 1 
000 000 001. At any moment, let x be the result of the last sum operation, or 
just 0 if there were no sum operations before. Then
∙ “+ i" means add((i + x) mod M),
∙ “- i" means del((i + x) mod M),
∙ “? i" means find((i + x) mod M),
∙ “s l r" means sum((l + x) mod M,(r + x) mod M).

**Output:** For each find request, just output “Found" or “Not found" (without 
quotes; note that the first letter is capital) depending on whether (i + x) mod 
M is in S or not. For each sum query, output the sum of all the values v in S 
such that ((l+x) mod M) ≤ v ≤ ((r+x) mod M) (it is guaranteed that in all the 
tests ((l+x) mod M) ≤ ((r+x) mod M)), where x is the result of the last sum 
operation or 0 if there was no previous sum operation.

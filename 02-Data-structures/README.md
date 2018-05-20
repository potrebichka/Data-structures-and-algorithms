##1-1. Check brackets in the code.
*Implement a feature for a text editor to find errors in the usage of brackets in the
code.*

**Input:** One string S.

**Output:** If the code in 𝑆 uses brackets correctly, output “Success" (without the 
quotes). Otherwise, output the 1-based index of the first unmatched closing bracket, and 
if there are no unmatched closing brackets, output the 1-based index of the first 
unmatched opening bracket.

##1-2. Compute tree height.
* You are given a description of a rooted tree. Your task is to compute and output its 
height. Recall that the height of a (rooted) tree is the maximum depth of a node, or the 
maximum distance from a leaf to the root. You are given an arbitrary tree, not necessarily 
a binary tree.*

**Input:** The first line contains the number of nodes n. The second line contains n 
integer numbers from −1 to n−1 — parents of nodes. If the i-th one of them (0 ≤ i ≤ n−1)  
is −1, node i is the root, otherwise it’s 0-based index of the parent of i-th node. It is 
guaranteed that there is exactly one root. It is guaranteed that the input represents a 
tree.

**Output:** The height of the tree.

##1-3. Network packet processing simulation.
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

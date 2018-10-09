## 1-1. Construct a Trie from a Collection of Patterns.
*Construct a trie from a collection of patterns.*

**Input:** An integer n and a collection of strings Patterns = {p_1, . 
. . , p_n} (each string is given on a separate line).

**Output:** The adjacency list corresponding to Trie(Patterns), in the 
following format. If Trie(Patterns) has n nodes, first label the root 
with 0 and then label the remaining nodes with the integers 1 through 
n-1 in any order you like. Each edge of the adjacency list of 
Trie(Patterns) will be encoded by a triple: the first two members of 
the triple must be the integers i, j labeling the initial and terminal 
nodes of the edge, respectively; the third member of the triple must be 
the symbol c labeling the edge; output each such triple in the format 
u->v:c (with no spaces) on a separate line.

## 1-2. Implement TrieMatching.
*Implement TrieMatching algorithm.*

**Input:** The first line of the input contains a string Text, the 
second line contains an integer n, each of the following n lines 
contains a pattern from Patterns = {p_1,. . . , p_n}.

**Output:** All starting positions in Text where a string from Patterns 
appears as a substring in increasing order (assuming that Text is a 
0-based array of symbols).

## 1-3. Extend TrieMatching.
*The goal in this problem is to extend the algorithm from the previous 
problem such that it will be able to handle cases when one of the 
patterns is a prefix of another pattern. In this case, some patterns 
are spelled in a trie by traversing a path from the root to an internal 
vertex, but not to a leaf.*

**Input:** The first line of the input contains a string Text, the 
second line contains an integer n, each of the following n lines  
contains a pattern from Patterns = {p_1, . . . , p_n}.

**Output:** All starting positions in Text where a string from Patterns 
appears as a substring in increasing order (assuming that Text is a 
0-based array of symbols). If more than one pattern  appears starting at 
position i, output i once.

## 1-4. Construct the Suffix Tree of a String.
*Build a suffix tree of the string text and return a list with all of 
the labels of its edges (the corresponding substrings of the text) in 
any order.*

**Input:** A string Text ending with a “$” symbol.

**Output:** The strings labeling the edges of SuffixTree(Text) in any 
order.

## 1-5. Find the Shortest Non-Shared Substring of Two Strings.
*Find the shortest substring of one string that does not appear in  
another string.*

**Input:** Strings Text1 and Text2.

**Output:** The shortest (non-empty) substring of Text1 that does not 
appear in Text2. (Multiple solutions may exist, in which case you may 
return any one.)

## 2-1. Construct the Burrows-Wheeler Transform of a String.
*Construct the Burrows_Wheeler transform of a string.*

**Input:** A string Text ending with a "$" symbol.

**Output:** BWT(Text).

## 2-2. Reconstruct a String from its Burrows-Wheeler Transform.

**Input:** A string *Transform* with a single "$" sign.

**Output:** The string *Text* such that BWT(*Text*) = *Transform*.

## 2-3. Implement BetterBWMatching.
*Implement BetterBWMAtching algorithm.*

**Input:** A string *BWT(Text)*, followed by an integer *n* and a collection of *n* strings *Patterns* = *{p_1,...,p_n}* (on one line separated by space).

**Output:** A list of integers, where *i*-th integer corresponds to the number of substring matches of the *i*-th member of *Patterns* in *Text*.

## 2-4. Construct the Suffix Array of a String.

**Input:** A string *Text* ending with a "$" symbol.

**Output:** *SuffixArray*(*Text*), that is, the list of starting positions (0-based) of sorted suffixes separated by spaces.

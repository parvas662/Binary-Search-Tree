# Ceil in BST
MediumAccuracy: 62.73% Submissions: 57K+ Points: 4


Given a BST and a number X, find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.

If Ceil could not be found, return -1.

Example 1:

Input:

          5
        /   \
       1     7
        \
         2 
          \
           3
       
X = 3
Output: 3
Explanation: We find 3 in BST, so ceil
of 3 is 3.
Example 2:

Input:

        10
       /  \
      5    11
     / \ 
    4   7
         \
           8
       
X = 6
Output: 7
Explanation: We find 7 in BST, so ceil
of 6 is 7.
Your task:
You don't need to read input or print anything. Just complete the function findCeil() to implement ceil in BST which returns the ceil of X in the given BST.

Expected Time Complexity: O(Height of the BST)
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1 <= Number of nodes <= 105
1 <= Value of nodes<= 105


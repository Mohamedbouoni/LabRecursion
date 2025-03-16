exercice 1 :
2. In the worst case, the recursive function can explore all possible subsets of the coin set
O(2**N)
3. Optimized Solution Using Dynamic Programming
O(N×M)
N → Amount to be changed
M → Number of coins
Memoization ensures each subproblem is solved only once

exercise 2 :
2. Recursive calls: For each recursive call, we reduce N by 1, making N recursive calls
3. 
Recursive Approach 
Time Complexity: O(N)
Space Complexity: O(N)

Iterative Approach
Time Complexity: O(N)
Space Complexity: O(1) 

exercise 3 :
2. Non-Tail-Recursive Factorial :
   Calls are nested before returning a result.
Each recursive call adds a new frame to the call stack, making it inefficient for large n.
Stack overflow risk for very large numbers.
Tail-Recursive Factorial :
  Uses an accumulator to store intermediate results.
  Recursive call is the last operation
3. all three approaches have a time complexity of O(n).
ail recursion doesn't require storing intermediate function calls.
The recursive call is the last operation, so no additional stack frame is needed (in languages with tail-call optimization)

exercise 4:
2. Complexity Analysis of Recursive Approach
Time Complexity: O(2ⁿ) 
Space Complexity: O(n) 

Complexity Analysis of Iterative Approach
Time Complexity: O(n²) 
Space Complexity: O(n²)

Bonus Challenge :
2. Move the top N-1 disks from the source rod to the auxiliary rod.
Move the Nth disk (the largest disk) directly from the source rod to the target rod.
Move the N-1 disks from the auxiliary rod to the target rod.
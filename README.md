# Students names and class
 Daniel Urbano Viana
 Juan David Mendiola
 class 3952


# System, Language, and Tools

OS: Windows.

Language: Python 3.

Tools: Visual Studio Code + Python extension + Python interpreter.

# how to Run in Visual Studio Code

Install Python from python.org.

Install VS Code and the Python extension.

Create a .py file, paste the code.

Select the Python interpreter in VS Code.

Run in terminal:
python filename.py

# Algorithm Explanation
The algorithm used is DFA Minimization via the Table-Filling Method (distinguishable pairs method):

Initialization:

Represent all possible pairs of states (i, j) with i < j.

Initially, assume all pairs are equivalent (can be merged).

Marking Non-Equivalent Pairs:

Mark as non-equivalent any pair where:

One state is a final (accepting) state, and the other is not.

Iterative Refinement:

Repeatedly check each pair (i, j):

For each symbol in the alphabet, find the next states (next_i, next_j).

If the next states are already known to be non-equivalent, mark (i, j) as non-equivalent.

Repeat until no changes occur.

Collect Equivalent Pairs:

After refinement, the remaining pairs marked as equivalent are output in lexicographic order.

Complexity:

Worst-case time complexity: O(n² · |Σ|),
where n = number of states, and |Σ| = size of the alphabet.

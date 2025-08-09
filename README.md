# Tarea1

System, Language, and Tools
Operating System: Compatible with Windows, macOS, or Linux (your choice; Python is cross-platform).

Programming Language: Python 3 (version 3.7 or higher recommended).

Tools:

Visual Studio Code (VS Code) as the IDE.

Python extension for VS Code.

Python interpreter installed locally.

-How to Run the Code in Visual Studio Code
Install Python:

Download and install Python from https://www.python.org/downloads/.

Ensure you check the option "Add Python to PATH" during installation.

Install Visual Studio Code:

Download and install VS Code from https://code.visualstudio.com/.

Install Python Extension in VS Code:

Open VS Code.

Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X on Mac).

Search for "Python" and install the one by Microsoft.

Create the Python File:

Open a folder in VS Code.

Create a new file, e.g., dfa_minimization.py.

Paste the Python code you have.

Select Python Interpreter:

Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac).

Search for "Python: Select Interpreter" and choose your installed Python version.

Run the Program:

Open a terminal in VS Code (View → Terminal or `Ctrl+``).

Run the program with:

python dfa_minimization.py






-Algorithm Explanation
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

# System, Language, and Tools

OS: Works on Windows, macOS, or Linux.

Language: Python 3.

Tools: Visual Studio Code + Python extension + Python interpreter.

# how to Run in Visual Studio Code

Install Python from python.org.

Install VS Code and the Python extension.

Create a .py file, paste the code.

Select the Python interpreter in VS Code.

Run in terminal:
python filename.py

# Algorithm

Goal: Find equivalent DFA states to minimize the automaton.

Mark pairs where one state is final and the other is not.

Iteratively check transitions; if they lead to a marked pair, mark them too.

Remaining unmarked pairs are equivalent.

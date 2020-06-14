# PYTHON MAZE SOLVER

## _Python project to solve maze using text file(file handling) and CLI(command line interface)_.

Program takes the input and output file name as command-line arguments.
Using the square matrix present in the `input.txt` file it would generate a path to reach the end of the maze and put it in the `output.txt` file.
***

**Technologies Involve**
>Project is implemented with `Python3` using [argparse](https://docs.python.org/3/library/argparse.html) module and to be run on CLI

**How to run**
>In the `input.txt` file, which contains the maze in the form of matrix of nxn size
>The program would work with CLI command specifying the details such as source file and destination file.
>A demo matrix is already present in `input.txt` file, you just need to overwrite it.


**Method of Approach**
>`Backtracing`
>Backtracking is basically checking all possibilities to get the optimal answer. Each time you reach to the root of any possibility, and find that it isn't optimal, you backtract, or just go to the next unsolved possibility in the program.
>For instance, consider that you are in a maze. You need to get out of it. You have some n paths in front of you. You don't know which gets you out. So you would try out all these different paths. Say you had 3 paths. Then you'll go to the 1st path. After being in this path, you'll have some more n paths from this sub-path. And this tree continues till some point. So if you check all the nodes that are led from the main 1st path, and not.
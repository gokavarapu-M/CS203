# Birthday Paradox

## Overview

This C++ program simulates Birthday Paradox and estimates minimum number of students required to achieve the given input probability of the event.
Here event refers to the case of two students having same birthday.

This calculation is done by simplifying and transforming the actual probabilty equation
$p = 1 - (^{365}C_k \cdot k!)/365^k $ 
 <br>   to <br>
$ \ln(1- p) = (365.5 - k)\cdot \ln(365/(365 - k)) - k $

## Code Explanation

- `LHS()`: Generates the LHS of simplfied equation.
- `RHS()`: Generates the RHS of simplfied equation.
- `FindK()`: Finds the minimum k for which LHS is aleast RHS

## Instructions

1. **Compile the Program**: Use a C++ compiler to compile the program.
2. **Run the Executable**: Execute the compiled program.
3. **Input**: Enter the probability of the event when prompted.
4. **Output**: The program will calculate and output the probability of a of two students having same birthday.

## Note

The simplification of above equation is done using stirling's approximation which states $\ln(n!) = 0.5\cdot\ln(2\pi) + (n+0.5)\ln(n) -n$

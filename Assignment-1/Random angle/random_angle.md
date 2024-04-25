# Bertrand's Paradox: Random Angle Method

## Overview

This C++ program simulates Bertrand's Paradox to estimate the probability of a randomly chosen chord in a circle being longer than the side length of an inscribed equilateral triangle. It utilizes the random angle method to generate chords.

## Code Explanation

- `RandomAngle()`: Generates a random angle in range 0 to Pi.
- `ChordLength(double radius, double angle)`: Calculates the length of the chord .
- `main()`: The main function of the program:
  - Seeds the random number generator with the current time.
  - Prompts the user to input the radius of the circle and the number of simulations.
  - Runs the simulations, counting the number of chords longer than the side length of the inscribed equilateral triangle.
  - Calculates the probability of a chord being longer than the side length of the triangle.

```cpp
event = a / (a + b);
```

where, a is the count of no.of.chords with length greater than side length
b is the count of no.of.chords with length less than side length

- Outputs the probability.

## Instructions

1. **Compile the Program**: Use a C++ compiler to compile the program.
2. **Run the Executable**: Execute the compiled program.
3. **Input**: Enter the radius of the circle and the number of simulations when prompted.
4. **Output**: The program will calculate and output the probability of a randomly chosen chord being longer than the side length of an inscribed equilateral triangle.

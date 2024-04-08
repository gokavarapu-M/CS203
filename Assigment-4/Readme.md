## Overview

This python script generates a sampler for _Gaussian distribution_ using inverse CDF method. It also plots a histogram using random numbers from a uniform distribution.

## Execution

To run the progrm use the following command

```python
python3 gaussian.py
```

1. After executing the command the the program asks for the inputs $\mu$, $\sigma$, $a$ and $b$.
2. Inputs should be a valid  i.e. $\sigma \ge 0$ and $a < b$.
3. After taking the inputs it generates a histogram of normalised area $1$ along with the theoritical gaussian distribution.

<br>
<br>

**Note:** This is a dynamic simulation outputs may vary for every run of the program.
**Reference:** We use this [_webpage_](<https://medium.com/mti-technology/how-to-generate-gaussian-samples-347c391b7959#:~:text=This%20method%20works%20by%20applying,one%20for%20y%20(U%E2%82%82).>) as reference to learn how to derive inverse CDF function for Gaussian distribution.

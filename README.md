# ProgrammingParadigm
Evidence 4 of the course Implementation of Computational methods

## Context

For this evidence, we will take a 1400 complexity problem from Codeforces known as "C. Theofanis' Nightmare"

The problem is about Theofanis who easily gets obsessed with problems before going to sleep and often has nightmares about them. To deal with his obsession he visited his doctor, Dr. Emix.

In his latest nightmare, he has an array a of size n and wants to divide it into non-empty subarrays such that every element is in exactly one of the subarrays. For example, the array [1,−3,7,−6,2,5] can be divided to [1][−3,7][−6,2][5]

The Cypriot value of such division is equal to Σki=1i⋅sumi where:

* k is the number of subarrays that we divided the array into 
* sumiis the sum of the i-th subarray.

The Cypriot value of this division of the array [1][−3,7][−6,2][5]=1⋅1+2⋅(−3+7)+3⋅(−6+2)+4⋅5=17.

Theofanis is wondering what is the maximum Cypriot value of any division of the array. An array b is a subarray of an array a if b can be obtained from a by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. In particular, an array is a subarray of itself.

For our input we will receive multiple lines of integers. The first line contains a single integer t(1≤t≤104) — the number of test cases.

Each test case consists of two lines.

The first line of each test case contains a single integer n (1≤n≤105) — the size of the array.

The second line contains n integers a1,a2,…,an (−108≤ai≤108) — the elements of the array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

So for example we will have this input

* 4 <- Number of arrays
* 6 <- Length of first array
* 1 -3 7 -6 2 5 <- First array
* 4 <- Lenght of second array
* 2 9 -5 -3 <- Second array
* 8 <- Length of third array
* -3 -4 2 -5 1 10 17 23 <- Third array
* 1 <- Length of fourth array
* 830 <- Fourth array

And for our output we will print one integer which is the maximum Cryopt value of the array 

32 <- Sum of first array
4 <- Sum of second array
343 <- Sum of third array
830 <- Sum of fourth array

So now that we have our problem we will implement a model for further analysis.

## Model

In order to solve this problem we will need to be creating different matrices, for each possible division of an array, each matrix will give us a Cryopt value and then after getting each Cryopt value we can compare them in order to get the maximum value.

So we will go step by step in order to build a dynamic table, some things to take into account for symbols:


* i will be an index that represents the number of elements considered from the start of the array.

* j will be an index that represents the number of subarrays the first 'i' elements are divided into.

 So for this table we will go step by step

 1. Initialization:

    dp[i][j] is initialized to -∞ for all i and j except dp[0][0] which is set to 0.
    This indicates that with zero elements and zero subarrays, the sum is zero.

 2. Prefix Sum Calculation:

    An auxiliary array prefix_sum is used where prefix_sum[i] stores the sum of the first i elements of the array.
    This helps in quickly calculating the sum of any subarray.

 3. Filling the DP Table:
    For each pair (i, j), the algorithm considers all possible previous subarray endings k (where k < i). It calculates the value dp[k][j-1] + j * (prefix_sum[i] - prefix_sum[k]).
    If this value is greater than the current dp[i][j], it updates dp[i][j] and records the subarray division in divs[i][j].


We will end up having this table:

       j
       0      1      2      3      ...    n
    +------+------+------+------+------+------+ 
  0 |    0 |  -∞  |  -∞  |  -∞  |  ... |  -∞  |  <- Inicialización
    +------+------+------+------+------+------+ 
  1 |  -∞  | dp[1][1] | dp[1][2] | dp[1][3] | ... | dp[1][n] |
    +------+------+------+------+------+------+ 
  2 |  -∞  | dp[2][1] | dp[2][2] | dp[2][3] | ... | dp[2][n] |
    +------+------+------+------+------+------+ 
  3 |  -∞  | dp[3][1] | dp[3][2] | dp[3][3] | ... | dp[3][n] |
    +------+------+------+------+------+------+ 
  . |  ... |  ... |  ... |  ... |  ... |  ... | 
  . |  ... |  ... |  ... |  ... |  ... |  ... | 
  n |  -∞  | dp[n][1] | dp[n][2] | dp[n][3] | ... | dp[n][n] |
    +------+------+------+------+------+------+

Let's test it, we will use this array: 1, -3, 7, -6, 2, 5

in which we will calculate dp[4][2], meaning all the possible ways to divide the array into 2 subarrays,so we would have this possible divisions

- [1,-3] [7,-6,2,5], whose operation is 1×(7−3)+2×(−6+2)+3×(5)=13
- [1, -3, 7] [-6,2,5] whose operation is 1×(7−3−6)+2×(2)+3×(5)=14

so if we fill the table with this solutions, we would get 

       j
       0    1     2     3     4     5     6
    +----+-----+-----+-----+-----+-----+-----+
  0 |  0 |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |
    +----+-----+-----+-----+-----+-----+-----+
  1 | -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |
    +----+-----+-----+-----+-----+-----+-----+
  2 | -∞ |  -∞ |  -∞  |  -∞ |  13 |  14 |  -∞ |
    +----+-----+-----+-----+-----+-----+-----+
  3 | -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |
    +----+-----+-----+-----+-----+-----+-----+
  4 | -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |
    +----+-----+-----+-----+-----+-----+-----+
  5 | -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |
    +----+-----+-----+-----+-----+-----+-----+
  6 | -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |  -∞ |
    +----+-----+-----+-----+-----+-----+-----+

and then we can fill each square with all the divisions and its result in order to determine the maximmum one.

## Implementation

In order to solve this code, we will create a python code in which we can take the inputs and output the maximum Cryopt value, for this code we will use parallel programming in order to get all the different array divisions in a parallel way in order to accelerate the process, the code will go as follows:

1. **Module Import**:
```python
import concurrent.futures
```
This line imports the `concurrent.futures` module, which allows for parallel execution of tasks.

2. **Function max_chipriota(arr)**:
```python
def max_chipriota(arr):
```
This function takes an input list of numbers `arr` and returns the maximum Chipriota sum and the corresponding divisions.

3. **Variable Initialization**:
```python
n = len(arr)
dp = [[-float('inf')]*(n+1) for _ in range(n+1)]
divs = [[[] for _ in range(n+1)] for _ in range(n+1)]
prefix_sum = [0]*(n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]
dp[0][0] = 0
```
Several lists and matrices are initialized, including `dp` (a matrix to store the values of the maximum Chipriota sum), `divs` (a matrix to store the corresponding divisions), and `prefix_sum` (a list to store the cumulative sums of `arr`).

4. **Function calculate_dp_and_divs(i, j)**:
```python
def calculate_dp_and_divs(i, j):
    for k in range(i):
        val = dp[k][j-1] + j*(prefix_sum[i]-prefix_sum[k])
        if val > dp[i][j]:
            dp[i][j] = val
            div = divs[k][j-1] + [arr[k:i]]
            divs[i][j] = div
```
This inner function calculates the values of `dp[i][j]` and `divs[i][j]` for a given pair of `i` and `j`.

5. **Parallel Task Execution**:
```python
with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(1, n+1):
        for j in range(1, i+1):
            executor.submit(calculate_dp_and_divs, i, j)
```
A `ThreadPoolExecutor` is used to execute the `calculate_dp_and_divs(i, j)` function in parallel for all possible pairs of `i` and `j`.

6. **Maximum Value Calculation**:
```python
max_j = max(range(n+1), key=lambda j: dp[n][j])
return dp[n][max_j], divs[n][max_j]
```
The maximum value in the last row of `dp` is found and this value along with the corresponding divisions are returned.

7. **Input Reading**:
```python
num_arrays = int(input())
arrays = []
for _ in range(num_arrays):
    length = int(input())
    array = list(map(int, input().split()))
    arrays.append(array)
```
The number of arrays is read and then each array.

8. **Calculation and Display of Results**:
```python
for arr in arrays:
    max_val, max_div = max_chipriota(arr)
    print(f"{max_val}")
```
For each array, the maximum Chipriota sum and the corresponding divisions are calculated using the `max_chipriota(arr)` function, and then the result is printed.

## Testing 

For this code there are two ways in order to test it.

First you can input manually the number of arrays and the arrays in the file "TheofanisNightmate.py", the input would need to be as follows:

```python
  4
  6
  1 -3 7 -6 2 5
  4
  2 9 -5 -3
  8
  -3 -4 2 -5 1 10 17 23
  1
  830
```

For this specific input, the expected output is

```python
  32
  4
  343
  830
```

So you can copy and paste this input in the code in order to test it.

The second way to test this program is by simply running the "AutomatizedNightmare.py" file, in this file the number of arrays and the arrays, after running this file the expected output would be

```python
  32
  4
  343
  830
```

## Complexity Analysis

## Other Implementations

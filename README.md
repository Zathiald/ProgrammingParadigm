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

## Implementation

## Testing 

## Complexity Analysis

## Other Implementations

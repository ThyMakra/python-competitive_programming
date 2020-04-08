# 1. Minimum distance that cover all Points around a Circle
## Instruction
There is a Circle.
- K = perimeters of the circle
- N = the number of points around it
For each point, the distance from the northest place (12 o'clock) to the point is given. 
- A-i = distance of point i-th
### + Find the minimum distance in order to connect all the points (dM)

## Examples
1. K = 20, N = 3, A = [5, 10, 15]
- => dm = 10
> Start at the 1st then go to the 2nd then the 3rd

2. K = 20, N = 3, A = [0, 5, 15]
- => dm = 10
> Start at 2nd then go to the 3rd then the 1st

## Code
```python
K = 20; N = 3; A = [5, 10, 15] # input

A += [K + A[0]] # add 1st(smallest) distance + 1 loop 
dM = K - max(y-x for x, y in zip(A, A[1:])) # Perimeter - Biggest difference of all points next to each other
dM
```
> \>>> 10
## Analysis
The minimum distance is : \
**Minimum distance = The perimeter - The biggest difference of all points next to each other**
> Example: If all the points occupy half of the circle then there will be an empty space. \
So **perimeter - biggest diff** is **perimeter - empty space**. We can get a line distance that covers all the points on the circle. \
> It could be any sides (left half, right half etc) since we also consider the _"smallest + 1 loop"_.

### Hint
- The maximum number of houses = 2 * 10^5
- We can loop each element without TLE (TL = 2s)

> atcoder Competition 160 - Task C

## What does zip do?
It takes multiple collection, it group it horizontally in to a list of tuples.
- note: 
    - Does not require the collections to be of the same length
    - The zipped-list's length follows the shortest list
    
### Code
```python
a = [1, 2, 3, 4]
b = [5, 6, 7]
c = [8, 9]

list(zip(a, b, c))
```
> \>>> [(1, 5, 8), (2, 6, 9)]
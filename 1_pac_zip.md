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
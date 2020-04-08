K = 20; N = 3; A = [5, 10, 15] # input

A += [K + A[0]] # add 1st(smallest) distance + 1 loop 
dM = K - max(y-x for x, y in zip(A, A[1:])) # Perimeter - Biggest difference of all points next to each other
print(dM)
import io
'''
Instruction: 
    There is a circular pond with houses around it.
    - K = perimeters of the pond
    - N = the number of houses around it
    For each houses, the distance from the northest point (12 o'clock) to the house is given. 
    - Ai = distance of house i-th

+ Find the minimum distance that needs to be traveled when you start at 1 of the houses and visith all the N houses

'''

'''
Examples 
    1. K = 20, N = 3, A = [5, 10, 15]
    => dm = 10
    - Start at the 1st then go to the 2nd then the 3rd

    2. K = 20, N = 3, A = [0, 5, 15]
    => dm = 10
    - Start at 2nd then go to the 3rd then the 1st
'''

# k,n,*a=map(int, open(0).read().split())
k = 20;n = 3;a = [5, 10, 15]


print('#' * 10, ' 1 ', '#' * 10) # 1
a += [k + a[0]]
print(a) # 1st house + 1 loop

print([y - x for x, y in zip(a, a[1:])])
'''
The minimum distance is 
The perimeter - The biggest difference of all houses next to each other

Example: If all the houses occupy half of the circle
'''    
# dm = k - max(y-x for x, y in zip(a, a[1:]))
# print(dm) # final result

a = [1,2 , 3, 4, 5, 6, 7]
b = [2, 3]



print('\n\n', '#' * 10, ' 2 ', '#' * 10) # 2
# print(min((l[i-1]-l[i])%k for i in range(n)))

'''
The hint in the exercise is :
    The maximum number of houses = 2 * 10^5
    So that we can loop each element without TLE (TL = 2s)
    
'''
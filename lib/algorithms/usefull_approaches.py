# map, filter, and reduce

# The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object and returns
#  a list containing all the function call results.

items = [1, 2, 3, 4, 5]
squared = []
for x in items:
    squared.append(x ** 2)
print(squared)

items = [1, 2, 3, 4, 5]
def sqr(x): return x ** 2
print(list(map(sqr, items)))

l = list(map((lambda x: x **2), items))
print(l)

print()

def square(x):
    return (x ** 2)
def cube(x):
    return (x ** 3)
funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print(list(value))

print()

# Because using map is equivalent to for loops, with an extra code we can always write a general mapping utility:
# Since it's a built-in, map is always available and always works the same way. It also has some performance benefit
#  because it is usually faster than a manually coded for loop.

def mymap(aFunc, aSeq):
    result = []
    for x in aSeq: result.append(aFunc(x))
    return result

print(list(map(sqr, [1, 2, 3])))
print(mymap(sqr, [1, 2, 3]))

print()

print(pow(2,10))
print(pow(3,11))
print(pow(4,12))
print(list(map(pow, [2, 3, 4], [10, 11, 12])))

print()

x = [1,2,3]
y = [4,5,6]
from operator import add
print(list(map(add, x, y)))

print()
print()

# filter and reduce

# As the name suggests filter extracts each element in the sequence for which the function returns True. The reduce
#  function is a little less obvious in its intent. This function reduces a list to a single value by combining
#  elements via a supplied function.

print(list(range(-5,5)))
print(list(filter((lambda x: x < 0), range(-5,5))))

# Here is another use case for filter(): finding intersection of two lists:

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x: x in a, b)))
# Note that we can do the same with list comprehension:
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print([x for x in a if x in b])


print()
print()
# The reduce is in the functools in Python 3.0. It is more complex. It accepts an iterator to process, but it's not
# an iterator itself. It returns a single result:

from functools import reduce
print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))
print(reduce((lambda x, y: x / y), [1, 2, 3, 4]))

# Here's the for loop version of the first of these calls, with the multiplication hardcoded inside the loop:
L = [1, 2, 3, 4]
result = L[0]
for x in L[1:]:
    result = result * x
print(result)


# Let's make our own version of reduce.

def myreduce(fnc, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = fnc(tally, next)
    return tally
print(myreduce( (lambda x, y: x * y), [1, 2, 3, 4]))
print(myreduce( (lambda x, y: x / y), [1, 2, 3, 4]))


import functools
L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
print(functools.reduce( (lambda x,y:x+y), L))
# We can get the same result by using join :
print(''.join(L))
# We can also use operator to produce the same result:
import functools, operator
print(functools.reduce(operator.add, L))
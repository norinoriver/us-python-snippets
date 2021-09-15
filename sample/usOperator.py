import operator
import itertools

print(2 + 3)
print(operator.add(2, 3))
print(operator.sub(2, 3))
print(operator.mul(2, 3))
print(operator.truediv(2, 3))
print(operator.floordiv(2, 3))
print(operator.lt(2, 3))
print(operator.le(2, 3))

l = [ i+1 for i in range(6)]
''' type of list '''
print(list(itertools.accumulate(l)))

''' type of tuple '''
print(tuple(itertools.accumulate(l)))

''' start last list data '''
print(list(itertools.accumulate(reversed(l))))
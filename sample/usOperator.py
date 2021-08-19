import operator
import itertools

print(2 + 3)

print(operator.add(2, 3))

l = [ i+1 for i in range(6)]
print(list(itertools.accumulate(l)))
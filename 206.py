__author__ = 'slyfocks'
from math import sqrt
# since the concealed square is 19 digits and starts with 1, integer must be 10 digits and must start with 1
# also, since the concealed square ends in a 0, integer must also end in 0
square_gen = (str(i ** 2) for i in xrange(1000000000, 1400000000, 10))
even_digits = range(2, 17, 2)
for i in square_gen:
    if all([i[even] == str(even / 2 + 1) for even in even_digits]):
        print "{}'s square root is {}".format(i, sqrt(int(i)))
        break

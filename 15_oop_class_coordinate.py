# Copyright (c) 2019 BIJU ALE

# Author: BIJU ALE (github.com/BijuAle)
# License: MIT License

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


class Coordinate:
    '''
    This is a class for a 2d coordinate,
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        xDiffSq = (self.x - other.x)**2
        yDiffSq = (self.y - other.y)**2
        return (xDiffSq + yDiffSq)**.5

    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)


c = Coordinate(3, 1)
o = Coordinate(2, 2)

print(c)
str(c)
help(c)

print(c.distance(o))
print(c.distance(o))

import sys
print(sys.getsizeof(c))
print(sys.getsizeof(o))

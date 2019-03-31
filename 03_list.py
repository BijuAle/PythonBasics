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

players = [12, 34, 63, 10, 8, 2]

# Add item to the end of list
players.append(12)

# Delete 1st two items
players[:2] = []

# Empty list
players[:] = []

# Iterating over list values while getting the index too
m = ['a', 'b', 'c', 'd']
for index, value in enumerate(m):
    print('{0}: {1}'.format(index, value))

# Find most frequent item
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key=test.count))

# List Comprehensions:

# Get list of sqaures of first 100 numbers
squares = [x**2 for x in range(1, 101)]
print(squares)

# Get remainders of squares of first 100 numbers divided by 5
remainders = [x**2 % 5 for x in range(1, 101)]
print(remainders)


# Get Movies with title starting with letter G
movies = ['Star Wars', 'Gandhi', 'Shawshank Redemption', 'Goodwill Haunting', 'Gone with the wind', 'Rear Windows']
movies2 = [title for title in movies if title.startswith('G')]
print(movies2)

# Get movies released before 2000
movies = [('Star Wars', 2000), ('Gandhi', 1999), ('Shawshank Redemption', 1990), ('Goodwill Haunting', 2001), ('Gone with the wind', 1966), ('Rear Windows', 1956)]
movies2 = [title for (title, year) in movies if year < 2000]
print(movies2)

# List as Vector - Scalar Multiplication
v = [2, -3, 1]
v2 = [x * 4 for x in v]
print(v2)

# Get cartesian product
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_prod = [(a, b) for a in A for b in B]
print(cartesian_prod)

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


def checkCart(cart, item):
    for i in cart:
        print(i)

    if item in cart:
        print('No need to buy ' + item)
    else:
        print("Buy " + item)
    print("\n")


cart = {"cheese", "ham", "sausage", "milk"}
checkCart(cart, 'ham')
checkCart(cart, 'oats')
checkCart(cart, 'honey')
checkCart(cart, 'cheese')


# Set operations can be performed
set_a = {1, 2, 3, 4, 5}
set_b = {2, 4, 5, 9}


# Intersection
print(set_a & set_b)

# Difference
print(set_a - set_b)
print(set_b - set_a)

# Union
print(set_a | set_b)

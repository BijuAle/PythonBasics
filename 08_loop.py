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

foods = ['cheese', 'bacon', 'beef', 'ham']


# for loop
def func1():
    for n in range(10):
        print(n)


def printAllFoods():
    for eachFood in foods:
        print(eachFood)
        print(len(eachFood))


def printSomeFoods():
    for eachItem in range(5, 12, 2):  # 5 - start, 12 - end, 2 - increment
        print(eachItem)


# While loop
def func2():
    danger = 2
    while danger < 10:
        print(danger, + "safe")  # Int - String concatenation
        danger += 1


# Can use Break & continue in loop

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

# Default value for parameter
def getGender(gender=None):
    if gender is 'm':
        print('Male')
    elif gender is 'f':
        print('Female')
    else:
        print(gender)


getGender('m')
getGender('f')
getGender()

# Keyword parameters
def printSentence(name='Jackson', action='makes', item='guitars'):
    print(name, action, item)


printSentence()
printSentence('John', 'bakes', 'pizza')
printSentence('Mary')
printSentence(action='repairs', name='Paul')


# Flexible parameter count
def addNums(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


addNums(2)
addNums(3, 44.2, 1)
addNums(234, 4, -5)

# Unpacking parameters
def healthCalc(args):
    result = (100 - args[0]) + (args[1] * 2.4) - (args[2] * 2)
    print(result)


args = [23, 123, 22]
healthCalc(args)

# Returning multiple values from a function
def getAString():
    a = "George"
    b = "is"
    c = "cool"
    return a, b, c


sentence = getAString()
(a, b, c) = sentence
print(a, b, c)

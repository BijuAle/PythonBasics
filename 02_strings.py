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

# Print as raw strin#G
print(r'C:/net')

# Escaping chars
print("This is the double quote symbol - \"\"")

name = "Roger Penrose"

# Print value of variable firstprint(name 5 times.
print((name + '\n') * 3)

# Print 1st letter from a string
print(name[0])

# Print 1st letter from a string from right
print(name[-1])

# Print letters from of a string from 2nd to 3rd pos
print(name[2:4])

# Print letters of a string from begining to 4th pos
print(name[:4])

# Print letters of a string from 4th pos to last pos
print(name[4:])

# Print length of a string
print(len(name))

# Reverse string
name = "George"
name = name[::-1]
print(name)

# Strip unwanted chars
name = "  George "
name2 = "George///"
name = name.strip()  # prints "George"
name2 = name2.strip("/")  # prints "George"
print(name)
print(name2)

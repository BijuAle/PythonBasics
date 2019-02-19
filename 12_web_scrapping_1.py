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

import random
import requests
import shutil


def downloadImage(uri):
    filename = str(random.randrange(1, 10000)) + '.jpg'
    r = requests.get(uri, stream=True, headers={'User-agent': 'Mozilla/5.0'})
    if r.status_code == 200:  # request suceeds
        with open(filename, 'wb') as f:  # open, process, close w-write, b-binary/image
            r.raw.decode_content = True  # decompress file
            shutil.copyfileobj(r.raw, f)  # copyfileobj(source, destination)


downloadImage('https://images.pexels.com/photos/349758/hummingbird-bird-birds-349758.jpeg?auto=compress&cs=tinysrgb&h=350')

# shutil - https://docs.python.org/2/library/shutil.html
# requests - http://docs.python-requests.org/en/master/user/quickstart/
# open() - https://docs.python.org/3/library/functions.html#open

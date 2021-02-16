
# Copyright (c) 2021 Venkata Ramana P (https://github.com/itsmepvr) <pvrreddy155@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Split any text with custom multiple delimitters and join them in the same way"""

"""
    Input: "any text,,with custom,,,multiple|delimiters
    Output: {"text": ["any text", "with custom", "multiple", "delimitters"], "delimitters": [",,", ",,,", "|"]}
"""

import re

class SplitAny:
    def __init__(self, text='', delimitters=[]):
        self.text = text
        self.delimitters = delimitters

    def parseText(self):
        delimitters = ['\\|' if x=='|' else x for x in self.delimitters]
        delimitters = "|".join(delimitters)
        textSplit = re.split('('+delimitters+')',self.text)
        textParse = {"text": [], "delimitter": []}
        for i, text in enumerate(textSplit):
            if not text in self.delimitters:
                textParse['text'].append(text)
            else:
                textParse['delimitter'].append(text)
        return textParse
    
    def joinParseText(self, textJson):
        text = textJson['text']
        delimitters = textJson['delimitter']
        output = ''
        for i, t in enumerate(text):
            output += t
            try:
                output += delimitters[i]
            except:
                output += ''
        return output

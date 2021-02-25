"""
Strings: Making Anagrams
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.
Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

Example

Delete  from  and  from  so that the remaining strings are  and  which are anagrams. This takes  character deletions.
Function Description
Complete the makeAnagram function in the editor below.
makeAnagram has the following parameter(s):
string a: a string
string b: another string
Returns
int: the minimum total characters that must be deleted
Input Format
The first line contains a single string, .
The second line contains a single string, .

Constraints

The strings  and  consist of lowercase English alphabetic letters, ascii[a-z].
Sample Input
cde
abc
Sample Output

4
Explanation
Delete the following characters from the strings make them anagrams:
Remove d and e from cde to get c.
Remove a and b from abc to get c.
It takes  deletions to make both strings anagrams.

"""

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d = defaultdict(int)
    for letter in a:
        d[letter] += 1
    for letter in b:
        d[letter] -= 1
    total = 0
    for letter in d:
        total += abs(d[letter])
    return total
a = 'cde'
b = 'abc'
print(makeAnagram(a, b))

stop = True
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     a = input()
#     b = input()
#     res = makeAnagram(a, b)
#     fptr.write(str(res) + '\n')
#     fptr.close()



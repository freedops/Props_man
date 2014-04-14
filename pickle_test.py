'''
Created on 9 Apr 2014

@author: scott
'''

import re

with open('test.txt', 'r') as read_file:
    pickle_jar = {}
    txt = read_file.read()
    lines = txt.split('\n')
    pattern = re.compile(r"""
     ^(?P<key>.+)        # key
     :\s*                # ignore : and whitespace
     (?P<value>[^\#].+\#*)?       # value
     (\#*\s*(?P<comment>.+)\s*)?              # ignore # and whitespace # comment

     """, re.VERBOSE)
    for line in lines:
        key = None
        value = None
        comment = None
        print(line)
        #key = re.search(pattern, line)

        try:
            parts = line.split(':')
            key = (parts[0]).strip()
            print (key)
            vals = ((parts[1]).strip()).split('#')
            value = (vals[0]).strip()
            if value=='':
                value = None
            comment = (vals[1]).strip()
        except IndexError:
            pass

        pickle_jar[key] = [value, comment]
        print(pickle_jar)

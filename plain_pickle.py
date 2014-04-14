'''
Created on 9 Apr 2014

@author: Scott Reeve

Copyright 2014 freedops.org

This file is part of the freedops.org tools collection.

The freedops.org tools collection is free software: you can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

The freedops.org tools collection is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with the freedops.org tools collection.

If not, see <http://www.gnu.org/licenses/>.
'''


class PlainPickle(object):
    '''
    A class to create and read sets of project parameters in a readable text
    format.
    The pickled files can be externally edited and re-read.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.pj = {}

    def save(self, name='params.txt'):
        '''
        Save an object to a text file
        '''
        try:
            with open(name, 'w') as save_file:
                return 0
        except:
            return 1

    def add(self, key, value=None, comment=None):
        '''
        Add a data set to an object
        '''
        self.pj[key] = [value, comment]

    def read(self, name):
        '''
        Read a plain text data file and try to extract information
        '''
        try:
            with open(name, 'r') as read_file:
                txt = read_file.read()
                lines = txt.split('\n')
                for line in lines:
                    key = None
                    value = None
                    comment = None
                    try:
                        parts = line.split(':')
                        key = (parts[0]).strip()
                        vals = ((parts[1]).strip()).split('#')
                        value = (vals[0]).strip()
                        if value == '':
                            value = None
                        comment = (vals[1]).strip()
                    except IndexError:
                        pass
                    self.add(key, value, comment)
            return 0
        except SyntaxError:
            return 1  # File read error
        except FileNotFoundError:
            return 2  # File not found error

    def clear(self):
        self.pj.clear()

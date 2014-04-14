'''
Created on 9 Apr 2014

@author: scott
'''
import unittest
import plain_pickle
import os.path


class Test(unittest.TestCase):

    def setUp(self):
        self.TestPickle = plain_pickle.PlainPickle()

    def tearDown(self):
        pass

    def testCreateFile(self):
        try:
            os.remove('params.txt')
        except:
            pass
        self.TestPickle.save()
        if not os.path.exists('params.txt'):
            assert False

    def testCreateFileNamed(self):
        try:
            os.remove('p.txt')
        except:
            pass
        self.TestPickle.save(name='p.txt')
        if not os.path.exists('p.txt'):
            assert False

    def testAddText(self):
        test_field = ['name', 'value', 'comment']
        self.TestPickle.add_field(test_field)

    def testReadFile(self):
        if self.TestPickle.read('test.txt'):
            assert False
        values = self.TestPickle.pj.get('key1')
        assert values[0] == 'value1'
        assert values[1] == 'comment 1 s d'
        # key and value, but no comment
        values2 = self.TestPickle.pj.get('key2')
        if values2:
            assert values2[0] == 'value2'
            assert values2[1] == None
        else:
            assert False
        values3 = self.TestPickle.pj.get('key3')
        if values3:
            assert values3[0] == None
            assert values3[1] == None
        else:
            assert False
        values4 = self.TestPickle.pj.get('key4')
        if values4:
            assert values4[0] == None
            assert values4[1] == 'comment adgag'
        else:
            assert False

    def testAddfield(self):
        pass


if __name__ == "__main__":
    import sys
    sys.argv = ['', 'Test.testCreateFile']
    unittest.main()

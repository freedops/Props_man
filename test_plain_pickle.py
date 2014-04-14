'''
Created on 9 Apr 2014

@author: scott
'''
import unittest
import plain_pickle
import os.path


class Test(unittest.TestCase):

    def setUp(self):
        #self.TestPickle = plain_pickle.PlainPickle()
        pass

    def tearDown(self):
        pass

    def testCreateFile(self):
        TestPickle = plain_pickle.PlainPickle()
        try:
            os.remove('params.txt')
        except:
            pass
        TestPickle.save()
        if not os.path.exists('params.txt'):
            assert False

    def testCreateFileNamed(self):
        TestPickle = plain_pickle.PlainPickle()
        try:
            os.remove('p.txt')
        except:
            pass
        TestPickle.save(name='p.txt')
        if not os.path.exists('p.txt'):
            assert False

    def testReadFile(self):
        TestPickle = plain_pickle.PlainPickle()
        if TestPickle.read('test.txt'):
            assert False
        values = TestPickle.pj.get('key1')
        assert values[0] == 'value1'
        assert values[1] == 'comment 1 s d'
        # key and value, but no comment
        values2 = TestPickle.pj.get('key2')
        if values2:
            assert values2[0] == 'value2'
            assert values2[1] == None
        else:
            assert False
        values3 = TestPickle.pj.get('key3')
        if values3:
            assert values3[0] == None
            assert values3[1] == None
        else:
            assert False
        values4 = TestPickle.pj.get('key4')
        if values4:
            assert values4[0] == None
            assert values4[1] == 'comment adgag'
        else:
            assert False

    def testAddfield(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_1', 'value_1', 'comment_1')
        value1 = TestPickle.pj.get('key_1')
        if value1:
            assert value1[0] == 'value_1'
            assert value1[1] == 'comment_1'
        else:
            assert False

    def testAddField2(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_2', None, 'comment_2')
        value2 = TestPickle.pj.get('key_2')
        if value2:
            assert value2[0] == None
            assert value2[1] == 'comment_2'
        else:
            assert False

    def testAddField3(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_3')
        value3 = TestPickle.pj.get('key_3')
        if value3:
            assert value3[0] == None
            assert value3[1] == None
        else:
            assert False

    def testAddField4(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_4', comment='as ge')
        value4 = TestPickle.pj.get('key_4')
        if value4:
            assert value4[0] == None
            assert value4[1] == 'as ge'
        else:
            assert False

    def testClear(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_4', comment='as ge')
        TestPickle.clear()
        value4 = TestPickle.pj.get('key_4')
        if value4:
            assert False

    def testSave(self):
        try:
            os.remove('params.txt')
        except:
            pass
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_1', 'value_1', 'comment_1')
        TestPickle.add('key_2', None, 'comment_2')
        TestPickle.add('key_4', None, 'comment_4')
        TestPickle.add('key_3')
        TestPickle.save()
        if not os.path.exists('params.txt'):
            assert False

if __name__ == "__main__":
    import sys
    sys.argv = ['', 'Test.testCreateFile']
    unittest.main()

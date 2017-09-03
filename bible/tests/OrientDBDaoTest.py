from dao.OrientDBDao import OrientDBDao
import unittest

class OrientDBDaoTest(unittest.TestCase):

    def setUp(self):
        self.dao = OrientDBDao()

    def testInsertNode(self):
        text = 'hello world'
        self.dao.insertTextNode({'TextID' : 'unittest', 'Text' : text})
        nodes = self.dao.findNode('unittest')
        for n in nodes:
            self.assertEqual(n.Text, text)


if __name__ == '__main__':
    unittest.main()
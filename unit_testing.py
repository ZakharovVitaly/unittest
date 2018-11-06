#!/usr/bin/python2
import unittest, re
def exp(a,b):
    try:
        a, b  = int(a), int(b)
        return a**b
    except ValueError: return None
def add(a,b):
    try: return a + b
    except TypeError: return None
def rmsp(strn):
    try:
        strn = str(strn)
        return re.sub('\s+', ' ', strn, re.M)
    except AttributeError: return None
class TestFuncs(unittest.TestCase):
    def test_exp_int(self): self.assertEqual(exp(2,5), 32)
    def test_exp_text(self): self.assertEqual(exp('4', '2'), 16)
    def test_exp_mix(self): self.assertEqual(exp(3, '2'), 9)
    def test_add_int(self): self.assertEqual(add(4,5), 9)
    def test_add_text(self): self.assertEqual(add('4','5'), '45')
    def test_add_mix(self): self.assertEqual(add('4',5), None)
    def test_rmsp_int(self): self.assertEqual(rmsp(4), '4')
    def test_rmsp_mix(self): self.assertEqual(rmsp('5    .   3'), '5 . 3')
if __name__ == '__main__': unittest.main(verbosity=2)

import unittest
import Assignment.primesInRange as primesInRange

class PrimeInRangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

# Sample happy path test
    def test100_100_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 2
        highBound = 10
        expectedResult = [2, 3, 5, 7]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
import unittest
import Assignment.primesInRange as primesInRange

class PrimeInRangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

# Happy paths :]
    def test4_22_VanillaNominalRange(self):
        lowBound = 4
        highBound = 22
        expectedResult = [5, 7, 11, 13, 17, 19]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    def test400_440_NominalRangeAndNamedParameters(self):
        lowBound = 400
        highBound = 440
        expectedResult = [401, 409, 419, 421, 431, 433, 439]
        actualResult = primesInRange.primesInRange(lowBound=lowBound, highBound=highBound)
        self.assertListEqual(expectedResult, actualResult)
    def test975_1000_NominalRangeAgainstUpperBound(self):
        lowBound = 975
        highBound = 1000 
        expectedResult = [977, 983, 991, 997]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    def test2_10_NominalRangeAgainstLowerBound(self):
        lowBound = 2
        highBound = 10
        expectedResult = [2, 3, 5, 7]

        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    def test601_601_EqualLowAndHighBoundIsPrime(self):
        lowBound = 601
        highBound = 601
        expectedResult = [601]

        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    def test42_42_EqualLowAndHighBoundIsNotPrime(self):
        lowBound = 42
        highBound = 42
        expectedResult = []

        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    def test524_540_NominalRangeNoPrimesPresent(self):
        lowBound = 524
        highBound = 540
        expectedResult = []
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)



# Sad paths :[

    def test1_10_LowBoundEqualsOneNominalHigh(self):
        lowBound = 1
        highBound = 10
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
    def test0_8_LowBoundLessThanOneNominalHigh(self):
        lowBound = 0
        highBound = 8
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
    def test500_1500_HighBoundOutOfRange(self):
        lowBound = 500
        highBound = 1500
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
    def testf_8_NonIntegerLowBound(self):
        lowBound = 'f'
        highBound = 8
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
    def test2_g_NonIntegerHighBound(self):
        lowBound = 2
        highBound = 4.5
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
    def testBlank_NoParametersGiven(self):
        expectedResult = None
        actualResult = primesInRange.primesInRange()
        self.assertEqual(expectedResult, actualResult)
    def test2_OneParameterGiven(self):
        lowBound = 2 
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound)
        self.assertEqual(expectedResult, actualResult)
    def test500_400_HighBoundLessThanLowerBound(self):
        lowBound = 500
        highBound = 400
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
    def test1_2000_BothBoundsOutOfRange(self):
        lowBound = -1
        highBound = 2000
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
    
    
    
    
    
    
    
    
    
    
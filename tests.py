# Ashley Owens
# CS 362 HW 1
# Black box testing assignment in which the tester does not have access to the source code. 
# This testing suite was created using the TSL Generator software using Category Partition Testing.


from unittest import TestCase
from credit_card_validator import credit_card_validator


class TestCC(TestCase):
    """
    Testing suite for the credit_card_validator function. Utilizes category partition testing for accurate credit card numbers for Visa, MC, and American Express. Also tests for accurate cc number lengths and valid checksum digits.
    Args:
        TestCase ([module]): python's unit testing module
    """
    def test1(self):
        """
        Utilizes category partition testing to assess credit card numbers of length = 0
        """
        self.assertFalse(credit_card_validator(""))

    def test2(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  3 Visa (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))

    def test3(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator(""))

    def test4(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))

    def test5(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  >16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))

    def test6(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  >16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))

    def test7(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  <16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test8(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  <16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))

    def test9(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  5 Visa (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test10(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  50 MC (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))

    def test11(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  51-55 MC
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator(""))

    def test12(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  51-55 MC
        Length   :  16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))

    def test13(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  51-55 MC
        Length   :  <16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test14(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  51-55 MC
        Length   :  <16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test15(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  51-55 MC
        Length   :  >16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test16(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  51-55 MC
        Length   :  >16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test17(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  56 MC (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test18(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  2220 MC (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))

    def test19(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  2221-2720 MC
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator(""))
    
    def test20(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  2221-2720 MC
        Length   :  16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))

    def test21(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  2221-2720 MC
        Length   :  <16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test22(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  2221-2720 MC
        Length   :  <16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test23(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  2221-2720 MC
        Length   :  >16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test23(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  2221-2720 MC
        Length   :  >16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test24(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  2721 MC (boundary case)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test25(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  33 AE (boundary case)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))

    def test26(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  34 AE
        Length   :  15
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator(""))
    
    def test27(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  34 AE
        Length   :  15
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test28(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  34 AE
        Length   :  <15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test29(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  34 AE
        Length   :  <15
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test30(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  34 AE
        Length   :  >15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test31(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  34 AE
        Length   :  >15
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test32(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  35 AE (boundary case)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test33(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  36 AE (boundary case)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test34(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  37 AE
        Length   :  15
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator(""))

    def test35(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  37 AE
        Length   :  15
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test35(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  37 AE
        Length   :  <15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test36(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  37 AE
        Length   :  <15
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test37(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  37 AE
        Length   :  >15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test38(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  37 AE
        Length   :  >15
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))

    def test39(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  38 AE (boundary case)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test40(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  0000
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))

















if __name__ == '__main__':
    unittest.main()
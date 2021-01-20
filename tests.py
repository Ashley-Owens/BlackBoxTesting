# Ashley Owens
# CS 362 HW 1
# Black box testing assignment in which the tester does not have access to the source code. This # testing suite was created using the TSL Generator software.


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
        Prefix   :  3 Visa
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
        Length   :  Too long
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))

    def test6(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  Too long
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))

    def test7(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  Too Short
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator(""))
    
    def test8(self):
        """
        Utilizes category partition testing to assess: 
        Prefix   :  4 Visa
        Length   :  Too Short
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator(""))


















if __name__ == '__main__':
    unittest.main()
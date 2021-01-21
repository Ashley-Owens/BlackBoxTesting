# Ashley Owens
# CS 362 HW 1: Black Box Testing
# This testing suite was created using the TSL Generator
# software using Category Partition Testing.
# Bug 1: The empty string
# Bug 2: Visa card number length <16 digits
# Bug 3: Valid Visa card number
# Bug 4: Invalid AE checksum digit
# Bug 5: AE card number length >15 digits
# Bug 6: Valid MC number with prefix = 2720

from unittest import TestCase
import unittest
from credit_card_validator import credit_card_validator


class TestCC(TestCase):
    """
    Testing suite for the credit_card_validator function. Utilizes
    category partition testing for accurate credit card numbers for
    Visa, MC, and American Express. Also tests for accurate cc number
    lengths and valid checksum digits.
    Args:
        TestCase ([module]): python's unit testing module
    """
    def test1(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  N/A
        Length   :  0
        CheckBit :  N/A
        """
        self.assertFalse(credit_card_validator(""))

    def test2(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  3 Visa (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("3539804460355539"))

    def test3(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  4 Visa (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("4115587550418370"))

    def test4(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  4 Visa
        Length   :  16
        CheckBit :  Invalid
        """
        self.assertFalse(credit_card_validator("4568964707043628"))

    def test5(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  4 Visa
        Length   :  >16
        CheckBit :  Invalid (checksum +1)
        """
        self.assertFalse(credit_card_validator("45689647070436284"))

    def test6(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  4 Visa
        Length   :  >16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("42429602404898163"))

    def test7(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  4 Visa
        Length   :  <16
        CheckBit :  Invalid (checksum -1)
        """
        self.assertFalse(credit_card_validator("401100920910868"))

    def test8(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  4 Visa
        Length   :  <16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("432575174663426"))

    def test9(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  5 Visa (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("5769518937345776"))

    def test10(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  50 MC (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("5058643112243685"))

    def test11(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  51 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("5197558500330773"))

    def test12(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  51-55 MC
        Length   :  16
        CheckBit :  Invalid (checksum +1)
        """
        self.assertFalse(credit_card_validator("5225708565886378"))

    def test13(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  51-55 MC
        Length   :  <16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("539697311627528"))

    def test14(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  51-55 MC
        Length   :  <16
        CheckBit :  Invalid (checksum -1)
        """
        self.assertFalse(credit_card_validator("540263173193798"))

    def test15(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  51-55 MC
        Length   :  >16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("55248743529581697"))

    def test16(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  51-55 MC
        Length   :  >16
        CheckBit :  Invalid (checksum +1)
        """
        self.assertFalse(credit_card_validator("55248743529581698"))

    def test17(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  56 MC (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("5628734430661863"))

    def test18(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2220 MC (boundary value)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("2220485273677826"))

    def test19(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2221 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("2221990220531538"))

    def test20(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2221-2720 MC
        Length   :  16
        CheckBit :  Invalid (checksum -1)
        """
        self.assertFalse(credit_card_validator("2321607081747478"))

    def test21(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2221-2720 MC
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("242133756959901"))

    def test22(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2221-2720 MC
        Length   :  15
        CheckBit :  Invalid (checksum +1)
        """
        self.assertFalse(credit_card_validator("252168668896427"))

    def test23(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2221-2720 MC
        Length   :  17
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("26211387573874428"))

    def test23(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2221-2720 MC
        Length   :  17
        CheckBit :  Invalid (checksum -1)
        """
        self.assertFalse(credit_card_validator("27209807658602866"))

    def test24(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2721 MC (boundary case)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("2721037771275191"))

    def test25(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  33 AE (boundary case)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("335938664968663"))

    def test26(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  34 AE (valid prefix)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("340283341164847"))

    def test27(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  34 AE
        Length   :  15
        CheckBit :  Invalid (checksum +1)
        """
        self.assertFalse(credit_card_validator("340283340064841"))

    def test28(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  34 AE
        Length   :  <15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("34063695431427"))

    def test29(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  34 AE
        Length   :  <15
        CheckBit :  Invalid (checksum -1)
        """
        self.assertFalse(credit_card_validator("34140996524230"))

    def test30(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  34 AE
        Length   :  >15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("3461749774119224"))

    def test31(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  34 AE
        Length   :  >15
        CheckBit :  Invalid (checksum +1)
        """
        self.assertFalse(credit_card_validator("3410776572135568"))

    def test32(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  35 AE (boundary case)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("355521870151772"))

    def test33(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  36 AE (boundary case)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("365521870151770"))

    def test34(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  37 AE (valid prefix)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("377991636901261"))

    def test35(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  37 AE
        Length   :  15
        CheckBit :  Invalid (checksum -1)
        """
        self.assertFalse(credit_card_validator("377881636901263"))

    def test35(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  37 AE
        Length   :  14
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("37233778147870"))

    def test36(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  37 AE
        Length   :  14
        CheckBit :  Invalid (checksum +1)
        """
        self.assertFalse(credit_card_validator("37233778147871"))

    def test37(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  37 AE
        Length   :  >15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("3759389287537694"))

    def test38(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  37 AE
        Length   :  >15
        CheckBit :  Invalid (checksum -1)
        """
        self.assertFalse(credit_card_validator("3759389287537693"))

    def test39(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  38 AE (boundary case)
        Length   :  15
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("384381529084162"))

    def test40(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  0000
        Length   :  16
        CheckBit :  Valid
        """
        self.assertFalse(credit_card_validator("0000000000000000"))

    def test41(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  52 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("5257193687554768"))

    def test42(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  53 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("5332207677321019"))

    def test43(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  54 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("5453936520873338"))

    def test44(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  55 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("5568657899972368"))

    def test45(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2720 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("2720996726400694"))

    def test46(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2621 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("2621136512752434"))

    def test47(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2521 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("2521131819156158"))

    def test48(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2421 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("2421480425073427"))

    def test49(self):
        """
        Utilizes category partition testing to assess:
        Prefix   :  2321 MC (valid prefix)
        Length   :  16
        CheckBit :  Valid
        """
        self.assertTrue(credit_card_validator("2321686910633480"))


if __name__ == '__main__':
    unittest.main()

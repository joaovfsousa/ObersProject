import unittest

from utils.cnpj_validator import cnpj_validator


class CnpjValidatorTest(unittest.TestCase):
  def test_valid_cnpj(self):
    a = cnpj_validator("04182131000198")
    b = cnpj_validator("76924624000167")
    print("AAAA", a, b, "AAAAA")
    self.assertTrue(a)
    self.assertTrue(b)

  def test_invalid_cnpj(self):
    self.assertFalse(cnpj_validator("12345678901234"))
    self.assertFalse(cnpj_validator("12345678901235"))

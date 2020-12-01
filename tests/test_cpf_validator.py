import unittest

from utils.cpf_validator import cpf_validator


class CpfValidatorTest(unittest.TestCase):
  def test_valid_cpf(self):
    self.assertTrue(cpf_validator("00809348039"))
    self.assertTrue(cpf_validator("97029857062"))

  def test_invalid_cpf(self):
    self.assertFalse(cpf_validator("12345678912"))
    self.assertFalse(cpf_validator("12345678913"))

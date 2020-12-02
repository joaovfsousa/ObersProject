def gen_first_digit(digits):
  result = 0
  baseValues = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

  for i in range(12):
    result += int(digits[i]) * baseValues[i]

  digit = 11 - (result % 11) if result % 11 >= 2 else 0
  return str(digit)


def gen_second_digit(digits):
  result = 0
  baseValues = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

  for i in range(13):
    result += int(digits[i]) * baseValues[i]

  digit = 11 - (result % 11) if result % 11 >= 2 else 0
  return str(digit)


def cnpj_validator(cnpj):
  cnpj = str(cnpj)
  if len(cnpj) != 14:
    return False

  digits = list(cnpj)

  first_digit = gen_first_digit(digits)

  if first_digit != digits[12]:
    return False

  second_digit = gen_second_digit(digits)

  print(second_digit, digits[13])
  if second_digit != digits[13]:
    return False
  else:
    return True

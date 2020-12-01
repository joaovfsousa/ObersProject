def gen_first_digit(digits):
  result = 0
  for i in range(1, 10):
    result += int(digits[i - 1]) * i

  digit = result % 11 if result % 11 != 10 else 0
  return str(digit)


def gen_second_digit(digits):
  result = 0

  for i in range(10):
    result += int(digits[i]) * i

  digit = result % 11 if result % 11 != 10 else 0
  return str(digit)


def cpf_validator(cpf):
  cpf = str(cpf)
  if len(cpf) != 11:
    return False

  digits = list(cpf)

  first_digit = gen_first_digit(digits)

  if first_digit != digits[9]:
    return False

  second_digit = gen_second_digit(digits)

  if second_digit != digits[10]:
    return False
  else:
    return True

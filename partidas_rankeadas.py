def is_between(value, min_value, max_value):
  """Returns True if the value is between the min_value and max_value, inclusive.

  Args:
    value: The value to check.
    min_value: The minimum value.
    max_value: The maximum value.

  Returns:
    True if the value is between the min_value and max_value, inclusive, False otherwise.
  """

  return min_value <= value <= max_value

def get_classe(xp):
  """Returns the class name for the given XP value.

  Args:
    xp: The XP value to check.

  Returns:
    The class name for the given XP value.
  """

  classe = None
  if is_between(xp, 0, 1000):
    classe = 'Ferro'
  elif is_between(xp, 1001, 2000):
    classe = 'Bronze'
  elif is_between(xp, 2001, 3000):
    classe = 'Prata'
  elif is_between(xp, 3001, 4000):
    classe = 'Ouro'
  elif is_between(xp, 4001, 5000):
    classe = 'Platina'
  elif is_between(xp, 5001, 6000):
    classe = 'Ascendente'
  elif is_between(xp, 6001, 7000):
    classe = 'Imortal'
  else:
    classe = 'Radiante'

  return classe

# Example usage:

table = [
  ('Fulano', 1500),
  ('Ciclano', 2500),
  ('Beltrano', 3500),
]

for nome, xp in table:
  classe = get_classe(xp)
  print(f'O Herói de nome: {nome} está no nível de {classe}')

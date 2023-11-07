# Potencia_Tech_iFood_Classificador_Nivel
Este projeto é um código Python que determina a classe de um herói, com base em seu número de pontos de experiência (XP). O código usa uma tabela de limites de XP para cada classe.

# Sumário

- [Classificador Heroi](#Classificador-Heroi)
  - [Output Heroi](#Output-Heroi)
- [Partidas Rankeadas](#Partidas-Rankeadas)
  - [Output Partida](#Output-Partida)
- [Escrevendo Classes](#Escrevendo-Classes)
  - [Output Classe](#Output-Classe)

# Classificador Heroi

```python
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

table = [
  ('Fulano', 1500),
  ('Ciclano', 2500),
  ('Beltrano', 3500),
]

for nome, xp in table:
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

  if classe is not None:
    print(f'O Herói de nome: {nome} está no nível de {classe}')
```

## Output Heroi

```
O Herói de nome: Fulano está no nível de Bronze
O Herói de nome: Ciclano está no nível de Prata
O Herói de nome: Beltrano está no nível de Ouro
```

# Partidas Rankeadas

```python
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
```

## Output Partida

```
O Herói de nome: Fulano está no nível de Bronze
O Herói de nome: Ciclano está no nível de Prata
O Herói de nome: Beltrano está no nível de Ouro
```

# Escrevendo Classes

```python

class Heroi:
  """Representa um heroi de uma aventura."""

  def __init__(self, nome, idade, tipo):
    """Inicializa as propriedades da classe."""
    self.nome = nome
    self.idade = idade
    self.tipo = tipo

  def atacar(self):
    """Exibe uma mensagem de ataque."""
    print(f"o {self.tipo.capitalize()} atacou usando {self.ataque_por_tipo()}")

  def ataque_por_tipo(self):
    """Retorna uma mensagem de ataque, conforme o tipo do herói."""
    ataques = {
        "mago": "magia",
        "guerreiro": "espada",
        "monge": "artes marciais",
        "ninja": "shuriken",
    }
    return ataques[self.tipo]


# Exemplo de uso

heroi = Heroi("Fulano", 30, "mago")
heroi.atacar()

heroi = Heroi("Ciclano", 30, "guerreiro")
heroi.atacar()

heroi = Heroi("Beltrano", 30, "monge")
heroi.atacar()

heroi = Heroi("Sicrano", 30, "ninja")
heroi.atacar()
```

## Output Classe

```
o Mago atacou usando magia
o Guerreiro atacou usando espada
o Monge atacou usando artes marciais
o Ninja atacou usando shuriken
```


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

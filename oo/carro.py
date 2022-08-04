

"""
Vodê deve cria uma classe que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade
ele oferece os seguintes atributos:
1) Atibuto de dado Velocidade
2) Metodo Acelerar, que deverá incrementar a velocidade em uma unidades.
3) Metodos frear, que deverá decrementar a velocidade em duas unidades.

a Direção terá a responsabilidade de
controlar a direção. ela oferece a os seguintes atributos:
1) valor de direção com valores possiveis: Norte, Sul, Leste, Oeste
2) Metodo Vira_a_direita
3) Metodo Vira_a_esquerda
  N
O   L
  S

    Exemplo
    >>> # testado o motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # testando direção

    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.virar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.virar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    3
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    1
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.virar_a_direita()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.virar_a_esquerda()
    >>> carro.calcular_direcao()
    'Sul'
"""

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def virar_a_direita(self):
        self.direcao.virar_a_direita()

    def virar_a_esquerda(self):
        self.direcao.virar_a_esquerda()


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def virar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def virar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)



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
    >>># testado o motor
    >>> motor = Motor()
    >>> motor.velocidade()
    0
    >>> motor.acelerar()
    >>> motor.velocidade()
    1
    >>> motor.acelerar()
    >>> motor.velocidade()
    2
    >>> motor.acelerar()
    >>> motor.velocidade()
    3
    >>> motor.frear()
    >>> motor.velocidade()
    1
    >>> motor.frear()
    >>> motor.velocidade()
    0
    >>># testando direção

    >>>direcao = Direcao()
    >>>direcao.valor()
    'Norte'
    >>>direcao.virar_a_direita()
    >>>direcao.valor()
    'Leste'
    >>>direcao.virar_a_direita()
    >>>direcao.valor()
    'Sul'
    >>>direcao.virar_a_direita()
    >>>direcao.valor()
    'Oeste'
    >>>direcao.virar_a_direita()
    >>>direcao.valor()
    'Norte'
    >>>direcao.virar_a_esquerda()
    >>>direcao.valor()
    'Oeste'
    >>>direcao.virar_a_direita()
    >>>direcao.valor()
    'Sul'
    >>>direcao.virar_a_direita()
    >>>direcao.valor()
    'Leste'
    >>>direcao.virar_a_direita()
    >>>direcao.valor()
    'Norte'
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
    >>> carro.frerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.frerar()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.virar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.virar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""

class Carro:
    pass

class Motor:
    pass

class Direcao:
    pass
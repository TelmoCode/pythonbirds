


class Pessoa:

    def __init__(self, *filhos, nome = None, idade=42):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    sophia = Pessoa(nome='Sophia')
    angelina = Pessoa(sophia, nome='Angelina')
    print(Pessoa.cumprimentar(angelina))
    print(id(angelina))
    print(angelina.cumprimentar())
    print(angelina.nome)
    print(angelina.idade)
    for filho in angelina.filhos:
        print(filho)



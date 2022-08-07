


class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=42):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 43

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos} '

class Menina(Pessoa):
    pass

if __name__ == '__main__':
    sophia = Menina(nome='Sophia')
    angelina = Pessoa(sophia, nome='Angelina')
    print(Pessoa.cumprimentar(angelina))
    print(id(angelina))
    print(angelina.cumprimentar())
    print(angelina.nome)
    print(angelina.idade)
    for filho in angelina.filhos:
        print(filho.nome)
    angelina.sobrenome = 'Ferreira'
    angelina.olhos = 1
    print(angelina.__dict__)
    print(sophia.__dict__)
    del angelina.filhos
    print(angelina.__dict__)
    print(sophia.__dict__)
    print(Pessoa.olhos)
    print(angelina.olhos)
    print(sophia.olhos)
    print(id(Pessoa.olhos), id(angelina.olhos), id(sophia.olhos))
    print(Pessoa.metodo_estatico(), angelina.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), angelina.nome_e_atributo_de_classe())
    pessoa = Pessoa("anonimo")
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Menina))
    print(isinstance(sophia, Pessoa))
    print(isinstance(sophia, Menina))





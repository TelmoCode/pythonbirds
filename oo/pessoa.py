


class Pessoa:

    def __init__(self, nome = None):
        self.nome = nome

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Clara')
    print(Pessoa.cumprimentar(p))
    print(dir(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Sophia'
    print(p.nome)


"""Calculadora."""


class Calculadora:

    def __init__(self, x: int = 0, y: int = 0):
        """Construtor da classe.

        Args:
            x(int): Primeiro valor informado
            y(int): Segundo valor informado
        """

        self.primeiro_numero = x
        self.segundo_numero = y

        # Verifica se os parâmetros informados são iguais a 0 para substituicao.
        if self.primeiro_numero == 0:
            self.primeiro_numero = 1
        if self.segundo_numero == 0:
            self.segundo_numero = 1

    def operacao(self, operacao_escolhida):
        """Funcao criada para direcionar para a operacao escolhida pelo usuário.

        Args:
            operacao_escolhida(int): Operacao que usuário escolheu fazer.
        """
        if operacao_escolhida == 1:
            return self.soma()
        elif operacao_escolhida == 2:
            return self.subtracao()
        elif operacao_escolhida == 3:
            return self.multiplicacao()
        elif operacao_escolhida == 4:
            return self.divisao()
        elif operacao_escolhida == 5:
            return self.exponenciacao()
        elif operacao_escolhida == 6:
            return self.modulo()

    def soma(self):
        """Funcao de soma"""
        return self.primeiro_numero + self.segundo_numero

    def subtracao(self):
        """Funcao de subtracao"""
        return self.primeiro_numero - self.segundo_numero

    def multiplicacao(self):
        """Funcao de multiplicacao"""
        return self.primeiro_numero * self.segundo_numero

    def divisao(self):
        """Funcao de divisao"""
        return self.primeiro_numero / self.segundo_numero

    def exponenciacao(self):
        """Funcao de exponenciacao"""
        return self.primeiro_numero ** self.segundo_numero

    def modulo(self):
        """Funcao de modulo"""
        return self.primeiro_numero % self.segundo_numero


if __name__ == '__main__':

    operacao = int(input(''
                         '\n1 - Soma '
                         '\n2 - Subtracao '
                         '\n3 - Multiplicacao '
                         '\n4 - Divisao '
                         '\n5 - Exponenciacao '
                         '\n6 - Modulo '
                         '\nDigite o número da operacao que deseja fazer: '))

    numero_1 = int(input('Digite o primeiro número: \n'))
    numero_2 = int(input('Digite o segundo número:  \n'))

    resultado = Calculadora(numero_1, numero_2).operacao(operacao_escolhida=operacao)
    print(f'O resultado da operacao é: {resultado}')

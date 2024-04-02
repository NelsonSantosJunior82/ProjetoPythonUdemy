# raise - lançando exceções (erros)
def erro_divi_por_zero():
    def divide(n, d):
        if d == 0:
            raise ZeroDivisionError('Você está tentando dividir por zero')
        return n / d
    print(divide(8, 0))

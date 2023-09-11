def metade(n, r=False):
    return n / 2 if r is False else moeda(n / 2)


def dobro(n, r=False):
    return n * 2 if r is False else moeda(n * 2)


def aumentar(p, n, r=True):
    return p / 100 * n + n if r is False else moeda((p / 100 * n) + n)


def diminuir(p, n, r=False):
    return n - (p / 100 * n) if r is False else moeda(n - (p / 100 * n))


def moeda(preço=0, moeda='R$'):
    return f"{moeda}{preço:.2f}".replace('-', '-')


def resumo(preço=0, a=0, d=0):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f"Preço anasalisado: \t{moeda(preço)}")
    print(f"Dobro do preço: \t{dobro(preço, True)}")
    print(f"Metade do preço: \t{metade(preço, True)}")
    print(f"{a}% de aumento: \t{aumentar(a, preço, True)}")
    print(f"{d}% de redução: \t{diminuir(d, preço, True)}")
    print('-' * 35)

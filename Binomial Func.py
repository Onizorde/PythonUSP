def fatorial(x):
    fat = 1
    while x != 0:
            fat = fat * x
            x = x - 1
    return fat

def binomial(n,k):
    if (n-k) <= 0:
        print("Valor binomial nulo")
    else:
        print("Valor binomial de ", fatorial(n) / (fatorial(k)*fatorial(n-k)))


def main():
    n = int(input("Digite valor de n: "))
    k = int(input("Digite valor de k: "))
    binomial(n,k)


def teste_fatorial(x):
    print(fatorial(x))


def teste_binomial(n,k):
    print(binomial(n,k))

main()

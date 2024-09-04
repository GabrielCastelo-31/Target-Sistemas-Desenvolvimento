MAX = 1000000


def fibonacci(n: int):
    n1, n2 = 0, 1
    for i in range(MAX):
        x = n2
        n2 = n1+n2
        n1 = x
        if n2 == n:
            return ("Pertence")
        if n2 > n:
            return ("Não pertence")
    return ("Não pertence ou valor muito grande.")


n = int(input())
if n < 0:
    print("Valor fora do intervalo permitido!")
else:
    print(fibonacci(n))

class Permutaciones:

    # Fórmula: rPn = n! / (n - r)!

    def permutacion(self):

        lista = {1, 2, 3, 4, 5, 6}
        r = 3

        p = Permutaciones()
        n = p.factorial(len(lista))

        if (r >= len(lista)):
            resultadoDeR = 1
        else:
            resultadoDeR = p.factorial(len(lista) - r)

        resultadoPermutacion = n / resultadoDeR
        print(resultadoPermutacion)

    def factorial(self, n):

        if (n == 0):
            return 1

        else:
            return self.factorial(n - 1) * n

def main():
    ejecutar = Permutaciones()
    ejecutar.permutacion()

if __name__ == '__main__':
    main()
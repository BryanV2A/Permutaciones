class Permutaciones:

    # Fórmula: rPn = n! / (n - r)!

    __lista = []
    __r = 0
    __resultadoPermutacion = 0

    def permutacion(self):

        self.__lista = {1, 2, 5, 6, 7, 8}
        self.__r = 3

        p = Permutaciones()
        n = p.factorial(len(self.__lista))

        if (self.__r >= len(self.__lista)):
            r = 1
        else:
            r = p.factorial(len(self.__lista) - self.__r)

        self.__resultadoPermutacion = n / r

        print(self.__resultadoPermutacion)

        return self.__resultadoPermutacion

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
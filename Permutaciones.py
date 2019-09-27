class Permutaciones:

    # Fórmula: Pn = n!

    def permutacion(self, n):

        if (n == 0):
            return 1

        else:
            return self.permutacion(n - 1) * n

def main():
    
    ejecutar = Permutaciones()
    r = ejecutar.permutacion(6)
    print(r)

if __name__ == '__main__':
    main()
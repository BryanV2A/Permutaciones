# Declaración de la clase Permutaciones
class Permutaciones:

    # Fórmula matemática de las permutaciones: rPn = n! / (n - r)!

    # Declración de un arreglo que almacena una lista de números n para realizar las permutaciones
    __lista = []

    # Variable del conjunto de ordenamiento de la permutaciones
    __r = 0

    # Variable que guarda el resultado
    __resultadoPermutacion = 0

    # Declaración del método permutacion
    def permutacion(self):

    # Asignacion de valores de las variables anteriormente mencionadas
        self.__lista = {1, 2, 5, 6, 7, 8}
        self.__r = 3

    # Creación de un objeto que acceda al método facotial y realize la operacion para asignarle el valor a n que es
    # el primer término de la operacion
        p = Permutaciones()
        n = p.factorial(len(self.__lista))

    # Sentencia if y else que identifican y asignan el valor para realizar el factorial del segundo término de la
    # fórmula para la division
        if (self.__r >= len(self.__lista)):
            r = 1
        else:
            r = p.factorial(len(self.__lista) - self.__r)

    # Variable para guardar el resultado de la operacion de permutaciones
        self.__resultadoPermutacion = n / r

    # Mensaje que imprime el resultado de la permutacion.
        print(self.__resultadoPermutacion)

        return self.__resultadoPermutacion

    # Método donde acceden las variables de n y r y realizan de forma recursiva ala operacion de obtencion de factorial
    def factorial(self, n):

        if (n == 0):
            return 1

        else:
            return self.factorial(n - 1) * n

# Método encargado de la ejecucion del programa accediendo al método permutacion donde se realiza parte del programa
def main():

    ejecutar = Permutaciones()
    ejecutar.permutacion()

# Sentencia que ejecuta al método main
if __name__ == '__main__':
    main()
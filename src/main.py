# main.py
class Calculator:
    def sum(self, a: int, b: int) -> int:
        return a + b

# Esto se ejecuta al correr main.py directamente
if __name__ == "__main__":
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    resultado = Calculator().sum(a, b)
    print(f"La suma es: {resultado}")

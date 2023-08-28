# calculadora

while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operation = input("Selecciona la operación (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
                continue
            result = num1 / num2
        else:
            print("Operación no válida. Inténtalo nuevamente.")
            continue

        print("Resultado:", result)

    except ValueError:
        print("Error: Ingresa números válidos.")
    except Exception as e:
        print("Error inesperado:", e)

    choice = input("¿Deseas realizar otra operación? (s/n): ")
    if choice.lower() != "s":
        break
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

print(multiply(1, 2))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](2, 4))

def calculator():
    should_accumulate = True
    num1 = float(input("Type your first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick a operation: ")
        num2 = float(input("Type your second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

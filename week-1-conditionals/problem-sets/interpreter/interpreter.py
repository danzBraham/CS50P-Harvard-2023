def main():
    print(interpret(input("Expression: ")))


def interpret(expression):
    x, op, y = expression.strip().split(" ")

    x = float(x)
    y = float(y)

    match op:
        case "+":
            return x + y
        case "-":
            return x - y
        case "/":
            return x / y
        case "*":
            return x * y
        case "%":
            return x % y


main()

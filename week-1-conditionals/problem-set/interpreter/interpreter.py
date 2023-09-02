# Ask user's prompt
x, y, z = input("Prompt: ").split(" ")

# Convert x and z to float
x = float(x)
z = float(z)

# Matching the y
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)

def calculate(a, b, operator="+"):
    if operator == "*":
        c = a * b
    elif operator == "/":
        c = a / b
    elif operator == "**":
        c = a ** b
    elif operator == "-":
        c = a - b

    return c

def to_infix(prefix):
    stack = []
    operators = ['+', '-', '*', '/']
    tokens = prefix.split()

    for token in reversed(tokens):
        if token in operators:
            if len(stack) < 2:
                raise ValueError("Недостаточно операндов для выполнения операции.")
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"({op1} {token} {op2})")
        else:
            stack.append(token)

    if len(stack) != 1:
        raise ValueError("Вы отправили пустую строку")

    return stack[0]

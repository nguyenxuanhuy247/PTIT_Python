
# def calc_postfix(expr):
#     stack = []
#     tokens = expr.split()
#     for token in tokens:
#         if token.isdigit():
#             stack.append(int(token))
#         elif token in ['+', '-', '*', '/']:
#             if len(stack) < 2:
#                 return "INVALID"
#             b = stack.pop()
#             a= stack.pop()
#             try:
#                 if token  == '+':
#                     stack.append(a + b)
#                 elif token == '-':
#                     stack.append(a - b)
#                 elif token == '*':
#                     stack.append(a * b)
#                 elif token == '/':
#                     stack.append(a / b)
#             except ZeroDivisionError:
#                 return "INVALID"
#         else:
#             return "INVALID"
#     return f"{stack[0]:.3f}" if len(stack) == 1 else "INVALID"


# t = int(input())
# for test in range(int(t)):
#     line = input()
# print(calc_postfix(line))



def calc_postfix(expr):
    stack = []
    tokens = expr.split()
    for token in tokens:
        try:
            num = int(token)
            stack.append(num)
        except ValueError:
            if token in ['+', '-', '*', '/']:
                if len(stack) < 2:
                    return "INVALID"
                b = stack.pop()
                a= stack.pop()
                try:
                    if token  == '+':
                        stack.append(a + b)
                    elif token == '-':
                        stack.append(a - b)
                    elif token == '*':
                        stack.append(a * b)
                    elif token == '/':
                        stack.append(a / b)
                except ZeroDivisionError:
                    return "INVALID"
            else:
                return "INVALID"    
    return f"{stack[0]:.5f}" if len(stack) == 1 else "INVALID"


t = int(input())
for test in range(int(t)):
    line = input()
    print(calc_postfix(line))
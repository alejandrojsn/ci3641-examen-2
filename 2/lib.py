from collections import deque
from typing import List

def op(c, x, y):
    if c == '+':
        return x + y
    elif c == '-':
        return x - y
    elif c == '*':
        return x * y
    elif c == '/':
        return x / y

def eval(exp: List[str], pre = False):
    stack = deque()
    exp = reversed(exp) if pre else exp
    for c in exp:
        if c in '+-*/':
            if len(stack) < 2:
                raise IndexError(f'Not enough operands for {c}')

            if pre:
                arg1, arg2 = stack.pop(), stack.pop()
            else:
                arg2, arg1 = stack.pop(), stack.pop()

            stack.append(op(c, arg1, arg2))
        elif c.isnumeric():
            stack.append(int(c))
        else:
            raise ValueError(f'Invalid token: {c}')
    
    return stack.pop()

def addParenthesis(c, arg, pos):
    match (c, arg[0], pos):
        case ('-', '-', 1) | \
             ('-', '+', 1) | \
             ('*', '+', _) | \
             ('*', '-', _) | \
             ('/', '+', _) | \
             ('/', '-', _) | \
             ('/', '*', 1) | \
             ('/', '/', 1):
            return f'({arg[1]})'
        case _:
            return arg[1]

def show(exp: List[str], pre = False):
    stack = deque()
    exp = reversed(exp) if pre else exp
    for c in exp:
        if c in '+-*/':
            if len(stack) < 2:
                raise IndexError(f'Not enough operands for {c}')

            if pre:
                arg1, arg2 = stack.pop(), stack.pop()
            else:
                arg2, arg1 = stack.pop(), stack.pop()

            arg1 = addParenthesis(c, arg1, 0)
            arg2 = addParenthesis(c, arg2, 1)

            stack.append((c, f'{arg1} {c} {arg2}'))
        elif c.isnumeric():
            stack.append((c, c))
        else:
            raise ValueError(f'Invalid token: {c}')

    return stack.pop()[1]

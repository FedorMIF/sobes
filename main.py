import itertools

def evaluate(expression):
    try:
        return eval(expression)
    except SyntaxError:
        return None

def generate_expressions():
    operators = ['+', '-', '']
    for ops in itertools.product(operators, repeat=9):
        expr = "".join(f"9{ops[0]}8{ops[1]}7{ops[2]}6{ops[3]}5{ops[4]}4{ops[5]}3{ops[6]}2{ops[7]}1{ops[8]}0")
        yield expr

for expr in generate_expressions():
    if evaluate(expr) == 200:
        print(expr)

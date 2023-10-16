def parse_E(tokens):
    if parse_T(tokens):
        if tokens and tokens[0] == '+':
            tokens.pop(0)
            return parse_E(tokens)
        return True
    return False

def parse_T(tokens):
    if parse_F(tokens):
        if tokens and tokens[0] == '*':
            tokens.pop(0)
            return parse_T(tokens)
        return True
    return False

def parse_F(tokens):
    if tokens and tokens[0] == '(':
        tokens.pop(0)
        if parse_E(tokens):
            if tokens and tokens[0] == ')':
                tokens.pop(0)
                return True
        return False
    elif tokens and tokens[0].isdigit():
        tokens.pop(0)
        return True
    return False

def parse(input_string):
    tokens = input_string.replace(' ', '')
    return parse_E(list(tokens))

# Test the parser
print(parse('3 + 4 * (5 + 6)'))  # Output: True
print(parse('3 + * 4'))  # Output: False

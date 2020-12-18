def operand_check(element, output_queu):
    if (element not in operator_dict.keys()) and (element not in parenthesis_dict.keys()):
        output_queu.append(element)

def parenthesis_check(element, stack, output_queu):
    if element == "(":
        stack.append(element)
    elif element == ")":
        while stack[-1] != "(":
            temp = stack.pop()
            output_queu.append(temp)
        stack.pop()

def operator_check(element, stack, output_queu):
    if element in operator_dict.keys():
        while (len(stack) != 0) and assoc_precedence_check(element, stack) and does_top_of_stack_have_operator(stack):
            temp = stack.pop()
            output_queu.append(temp)
        stack.append(element)

def assoc_precedence_check(element, stack):
    if stack[-1] == "(" or ((operator_assoc[element] == 0) and (operator_dict[element] <= operator_dict[stack[-1]])): return True
    elif stack[-1] == "(" or ((operator_assoc[element]==1) and (operator_dict[element] < operator_dict[stack[-1]])): return True
    else: return False

def does_top_of_stack_have_operator(stack):
    return True if stack[-1] in operator_dict.keys() else False

def empty_stack(stack, output_queu):
    while len(stack) != 0 :
        temp = stack.pop()
        output_queu.append(temp)
    return output_queu, stack

def evaluate(expression, stack, output_queu):
    for element in expression:
        if element == " ":
            continue
        operand_check(element, output_queu)
        parenthesis_check(element, stack, output_queu)
        operator_check(element, stack, output_queu)
    output_queu, stack = empty_stack(stack, output_queu)
    return output_queu, stack

def parse_rpn(stack):
    rpnstack = []
    for d in stack:
        if d.isnumeric():
            rpnstack.append(int(d))
        else:
            v2 = rpnstack.pop()
            v1 = rpnstack.pop()
            rpnstack.append(eval(f"{v1}{d}{v2}"))
    return rpnstack[0]

if __name__ == "__main__":
    # operators and precedences can be changed according to taste and purpose
    operator_dict = {"^": 3,
                    "*": 2,
                    "/": 2,
                    "+": 1,
                    "-": 1,
                    }

    parenthesis_dict = {
                "(":1,
                ")":0
    }
    # left = 0, right = 1
    operator_assoc = {"^": 1,
                  "*": 0,
                  "/": 0,
                  "+": 0,
                  "-": 0,
                  "(": 0,
                  ")": 0,
                  }

    output, _ = evaluate("1 + 2*(3-4)/(4-5)", [], [])
    print(parse_rpn(output))
    # usage guide:
    # WARNING, UGLY CODE ALERT! Might work, might not, might be super slow, might not. 
    # Has worked as far as i have tested it.
    # Always worth a shot if a parsing exercise comes up. Adjust precedences and associativities in 
    # operator_dict and operator_assoc. Mess with parenthesis_dict at own risk.
    # If it doesn't work, try changing some settings. If that doesn't work, maybe take it as a basis to build further on
    # (although further development and debugging might be hard courtesy of the spaghetti-code).
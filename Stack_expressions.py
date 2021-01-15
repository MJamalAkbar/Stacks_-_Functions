list_nbr = list(input("enter a expression= "))
print(f"let me check this expression is valid or not =", ''.join([str(element) for element in list_nbr]))
"""2+3+(6*2)"""


def first_operator(exp):
    if (exp[0] in ['*', '/', '}', ')', ']']):
        # print("Not valid expression")
        return True
    else:
        # print("valid expression")
        return False


def last_operator(exp):
    if (exp[-1] in ['+', '-', '*', '/', '(', '{', '[']):
        # print("Not valid expression")
        return True
    else:
        # print("valid expression")
        return False


def double_operators(exp):
    result = True
    for i in range(0, len(exp)):
        if (exp[i] in ['+', '-', '*', '/']) and (exp[i + 1] in ['+', '-', '*', '/']):
            result = False
    # print(result)
    return result


def empty_paranthesis(exp):
    result = True
    for i in range(0, len(exp)):
        if (exp[i] in ['(', '{', '[']) and (exp[i + 1] in [')', '}', ']']):
            return False  # invalid

    return result


def Paranthesis(exp):
    stack1 = []
    for i in list_nbr:
        # print(stack1)
        stack1.append(i)
    print("Push in Stack=> ", stack1)

    a = 0
    b = 0
    c = 0
    d = 0
    for j in stack1:
        temp = stack1.pop()
        if (temp == "("):
            a += 1
        elif (temp == "{"):
            c += 1
        elif (temp == "}"):
            d += 1
        elif (temp == ")"):
            b += 1
    if (a == b and c == d):
        # print("Valid statement")
        return False
    else:
        # print("invalid statement")
        return True


operators = ['+', '-', '*', '/']
Not_valid = True
first_opr = first_operator(list_nbr)
last_opr = last_operator(list_nbr)
double_word = double_operators(list_nbr)
pranthesis = Paranthesis(list_nbr)
empty_paran = empty_paranthesis(list_nbr)

if first_opr is True:
    print("Invalid First operator")
elif last_opr is True:
    print("Invalid Last Operator")
elif double_word is False:
    print("Invalid Double Word")
elif pranthesis is True:
    print("Invalid Paranthesis")
elif empty_paran is False:
    print("empty paranthesis")
else:
    print("Valid Expresssion")

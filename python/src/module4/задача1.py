def psp(stroka):
    stack = list()
    extra_parenthesis = 0
    for i in stroka:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                extra_parenthesis = extra_parenthesis + 1
    return len(stack) + extra_parenthesis

if __name__ == "__main__":
    stroka = input()
    print(psp(stroka))
    
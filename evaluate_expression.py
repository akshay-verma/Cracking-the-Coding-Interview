
from stack import Stack

precedence = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0, ")": 0}


def evaluateInfixExpression(expression):

    def getValue():
        if valStack.isEmpty():
            raise AssertionError("Invalid expression! Value stack is empty")
        return valStack.pop()

    def performOperation():
        operator = opStack.pop()
        val1 = getValue()
        val2 = getValue()
        valStack.push(str(eval(val2 + operator + val1)))

    valStack = Stack()
    opStack = Stack()
    for char in expression:
        try:
            _ = int(char)
            valStack.push(char)
            continue
        except ValueError:
            if char == "(":
                opStack.push(char)
            elif char == ")":
                while(not opStack.isEmpty() and opStack.peek() != "("):
                    performOperation()
                opStack.pop()
            else:
                while(not opStack.isEmpty() and precedence[opStack.peek()] >= precedence[char]):
                    performOperation()
                opStack.push(char)
    while(not opStack.isEmpty()):
        performOperation()
    return float(valStack.pop())


if __name__ == "__main__":
    expression = "1+(2*3)+(14/7)-1"
    result = evaluateInfixExpression(expression)
    print(result, result == eval(expression))

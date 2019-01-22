
from stack import Stack


def checkParenthesis(string):
    st = Stack()
    for char in string:
        if char == "(":
            st.push(char)
        elif char == ")":
            if st.isEmpty():
                return False
            st.pop()
    return st.isEmpty()


if __name__ == "__main__":
    string = "(a+((b*c))+e)))"
    string = "(((a)))"
    string = "((a)(b)(c+d)(e*(f+g))"
    result = checkParenthesis(string)
    print(result)

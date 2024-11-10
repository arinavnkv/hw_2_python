def check(brackets):
    bracket = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in brackets:
        if char in bracket:
            stack.append(char)
        elif not stack or bracket[stack.pop()] != char:
            return False

    return len(stack) == 0


a = '(({[]}))'
b1 = '{(})'
c = '([])[[]]'
b2 = ')())[[]]'
b3 = '(())[[]]'
b4 = '([])'

print(a, '=', check(a))
print(b1, '=', check(b1))
print(c, '=', check(c))
print(b2, '=', check(b2))
print(b3, '=', check(b3))
print(b4, '=', check(b4))
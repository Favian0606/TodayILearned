from decorators import timer

input_one = "()"
input_two = "()[]{}"
input_three = "(]"
input_four = "([)]"
input_five = "{[]}"


@timer
def is_valid_parentheses(s: str) -> bool:
    stack = []
    map_table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in map_table:  # open bracket
            stack.append(char)
        elif not stack or map_table[char] != stack.pop():
            return False

    return len(stack) == 0  # check consumption state; all are match if len is zero


print(is_valid_parentheses(input_one))
print(is_valid_parentheses(input_two))
print(is_valid_parentheses(input_three))
print(is_valid_parentheses(input_four))
print(is_valid_parentheses(input_five))

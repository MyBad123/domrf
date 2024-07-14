import sys
import datetime
from file_work import File


def check_brackets(some_str: str) -> bool:
    stack = []

    for char in some_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0


file_name: str = datetime.datetime.now().strftime('%H:%M %d.%m.%Y')
File().create_file(file_name, check_brackets(sys.argv[1]))

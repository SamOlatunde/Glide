import PySimpleGUI as sg

# Define toolbox commands: each category maps command names to code snippets.
toolbox_commands = {
    "Basics": {
        "Print": "print('Hello, world!')",
        "Make Variable": "x = 5",
        "Make Multiple Variables": "a, b, c = 1, 2, 3",
        "Basic Input": "name = input('Enter your name: ')\nprint('Hello,', name)",
        "Input with Conversion": "age = int(input('Enter your age: '))\nprint('In 5 years you will be', age + 5)",
        "False": "flag = False",
        "True": "status = True",
        "None": "value = None",
    },
    "Math Operations": {
        "Addition": "x = 5 + 3\nprint('Result:', x)",
        "Subtraction": "x = 10 - 4\nprint('Result:', x)",
        "Multiplication": "x = 6 * 7\nprint('Result:', x)",
        "Division": "x = 20 / 4\nprint('Result:', x)",
        "Integer Division": "x = 20 // 3\nprint('Result:', x)",
        "Exponentiation": "x = 2 ** 3\nprint('Power:', x)",
        "Increment by value": "x = 1\nx += 1\nprint(x)",
        "Decrement by value": "x = 2\nx -= 1\nprint(x)"
    },
    "Logical Operators": {
        "and": "x = True and False\nprint(x)",
        "or": "x = True or False\nprint(x)",
        "not": "x = not True\nprint(x)",
    },
    "Conditionals": {
        "if Statement": "x = 15\nif x > 10:\n    print('X is large')",
        "if-else Statement": "x = 5\nif x > 10:\n    print('X is large')\nelse:\n    print('X is small')",
    },
    "Loops": {
        "For Loop": "for i in range(5):\n    print(i)",
        "While Loop": "x = 0\nwhile x < 5:\n    print(x)\n    x += 1",
    },
    "Functions": {
        "Define Fruitless Function": "def greet():\n    print('Hi there!')",
        "Define Fruitful Function": "def add(a, b):\n    return a + b",
        "Function Call": "greet()\n# or add(2, 3)",
    },
    "File Operations": {
        "open()": "file = open('file.txt', 'r')",
        "file.write()": "file = open('file.txt', 'w')\nfile.write('Hello')",
        "file.close()": "file = open('file.txt', 'r')\nfile.close()",
    },
}

def get_toolbox_tree():
    # Tree setup
    toolbox_data = sg.TreeData()
    for category, items in toolbox_commands.items():
        toolbox_data.Insert("", category, category, [])
        for name, code in items.items():
            toolbox_data.Insert(category, name, name, [code])
    return toolbox_data
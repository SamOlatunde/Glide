import PySimpleGUI as sg

# Define toolbox commands: each category maps command names to code snippets.
toolbox_commands = {
    "Basics": {
        "Print": "print('Hello, world!')",
        "Make Variable": "x = 5",
        "Declare multiple Variables": "a, b, c = 1, 2, 3",
        "False": "flag = False",
        "True": "status = True",
        "None": "value = None",
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
    "File Operations": {
        "open()": "file = open('file.txt', 'r')",
        "file.write()": "file = open('file.txt', 'w')\nfile.write('Hello')",
        "file.close()": "file = open('file.txt', 'r')\nfile.close()",
    },
    "Input/Output": {
        "Basic Input": "name = input('Enter your name: ')\nprint('Hello,', name)",
        "Input with Conversion": "age = int(input('Enter your age: '))\nprint('In 5 years you will be', age + 5)",
    },
}

def get_toolbox_tree():
    toolbox_data = sg.TreeData()
    toolbox_data.Insert("", "Basics", "Basics", [])
    toolbox_data.Insert("", "Conditionals", "Conditionals", [])
    toolbox_data.Insert("", "Loops", "Loops", [])
    toolbox_data.Insert("", "Functions", "Functions", [])

    toolbox_data.Insert("Basics", "Print", "Outputs text or variables to the screen.", [])
    toolbox_data.Insert("Basics", "Make Variable", "Make a Variable", [])
    toolbox_data.Insert("Basics", "Declare Multiple Variables", "Assigns multiple values at once.", [])
    toolbox_data.Insert("Basics", "False", "Boolean value representing falsehood.", [])
    toolbox_data.Insert("Basics", "True", "Boolean value representing truth.", [])
    toolbox_data.Insert("Basics", "None", "Represents no value or null.", [])
    toolbox_data.Insert("Logical Operators", "and", "Logical AND operator", [])
    toolbox_data.Insert("Logical Operators", "or", "Logical OR operator", [])
    toolbox_data.Insert("Logical Operators", "not", "Logical NOT operator", [])
    toolbox_data.Insert("Conditionals", "if Statement", "Conditional statement", [])
    toolbox_data.Insert("Conditionals", "if-else Statement", "if else conditional statement", [])
    toolbox_data.Insert("Loops", "For Loop", "For Loop", [])
    toolbox_data.Insert("Loops", "While Loop", "While Loop", [])
    toolbox_data.Insert("Functions", "Define Fruitless Function", "Define function without a return value", [])
    toolbox_data.Insert("Functions", "Define Fruitful Function", "Define function with a return value", [])
    toolbox_data.Insert("Functions", "Function Call", "Function Call", [])
    toolbox_data.Insert("Math Operations", "Addition", "Addition", [])
    toolbox_data.Insert("Math Operations", "Subtraction", "Subtraction", [])
    toolbox_data.Insert("Math Operations", "Multiplication", "Multiplication", [])
    toolbox_data.Insert("Math Operations", "Division", "Division", [])
    toolbox_data.Insert("Math Operations", "Integer Division", "Integer division", [])
    toolbox_data.Insert("Math Operations", "Exponentiation", "Raise to a power", [])
    toolbox_data.Insert("Math Operations", "Increment by value", "Increment by value", [])
    toolbox_data.Insert("Math Operations", "Decrement by value", "Decrement by value", [])
    toolbox_data.Insert("File Operations", "open()", "Open input file", [])
    toolbox_data.Insert("File Operations", "file.write()", "Write to input file", [])
    toolbox_data.Insert("File Operations", "file.close()", "Close input file", [])
    toolbox_data.Insert("Input/Output", "Basic Input", "Basic Input", [])
    toolbox_data.Insert("Input/Output", "Input With Conversion", "Input with Conversion", [])
    return toolbox_data
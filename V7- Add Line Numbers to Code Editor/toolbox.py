import PySimpleGUI as sg

# Define toolbox commands: each category maps command names to code snippets.
toolbox_commands = {
    "Basics": {
        "Comment":"# <Enter Comment Here>",
        "Print": "print('<Enter Value or Variable Name Here>')",
        "Make Variable": "<Variable Name Here> = <Value or Variable Name Here>",
        "Declare multiple Variables": "a, b, c = 1, 2, 3",
        "Bool": "<Enter Variable Name> = <Enter a boolean value (True/False)>",
        "Input": "<Variable Name> = input('<Enter prompt for user>')",
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
}

def get_toolbox_tree():
    toolbox_data = sg.TreeData()
    toolbox_data.Insert("", "Basics", "Basics", [])
    toolbox_data.Insert("", "Logical Operators", "Logical Operators", [])
    toolbox_data.Insert("", "Conditionals", "Conditionals", [])
    toolbox_data.Insert("", "Loops", "Loops", [])
    toolbox_data.Insert("", "Functions", "Functions", [])
    toolbox_data.Insert("", "Math Operations", "Math Operations", [])

    toolbox_data.Insert("Basics", "Comment", "Comment", [])
    toolbox_data.Insert("Basics", "Print", "Print", [])
    toolbox_data.Insert("Basics", "Make Variable", "Make a Variable", [])
    toolbox_data.Insert("Basics", "Declare multiple Variables", "Make multiple Variables", [])
    toolbox_data.Insert("Basics", "Bool", "Declare a boolean", [])
    toolbox_data.Insert("Basics", "Input", "Input", [])
    toolbox_data.Insert("Logical Operators", "and", "AND", [])
    toolbox_data.Insert("Logical Operators", "or", "OR", [])
    toolbox_data.Insert("Logical Operators", "not", "NOT", [])
    toolbox_data.Insert("Conditionals", "if Statement", "if statement", [])
    toolbox_data.Insert("Conditionals", "if-else Statement", "if-else statement", [])
    toolbox_data.Insert("Loops", "For Loop", "For Loop", [])
    toolbox_data.Insert("Loops", "While Loop", "While Loop", [])
    toolbox_data.Insert("Functions", "Define Fruitless Function", "Function with Return", [])
    toolbox_data.Insert("Functions", "Define Fruitful Function", "Function without return", [])
    toolbox_data.Insert("Functions", "Function Call", "Function Call", [])
    toolbox_data.Insert("Math Operations", "Addition", "Addition", [])
    toolbox_data.Insert("Math Operations", "Subtraction", "Subtraction", [])
    toolbox_data.Insert("Math Operations", "Multiplication", "Multiplication", [])
    toolbox_data.Insert("Math Operations", "Division", "Division", [])
    toolbox_data.Insert("Math Operations", "Integer Division", "Integer division", [])
    toolbox_data.Insert("Math Operations", "Exponentiation", "Raise to a power", [])
    toolbox_data.Insert("Math Operations", "Increment by value", "Increment by value", [])
    toolbox_data.Insert("Math Operations", "Decrement by value", "Decrement by value", [])

    return toolbox_data
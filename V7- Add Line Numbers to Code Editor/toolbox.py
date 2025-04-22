import PySimpleGUI as sg

# Define toolbox commands: each category maps command names to code snippets.
toolbox_commands = {
    "Basics": {
        "Comment":"# <Enter Comment Here>",
        "Print": "print('<Enter Value or Variable Name Here>')",
        "Make Variable": "<Variable Name Here> = <Value or Variable Name Here>",
        "Declare multiple Variables": "a, b, c = 1, 2, 3",
        "Input": "<Variable Name> = input('<Enter prompt for user>')",
    },
    "Logical Operators": {
        "and": "<Conditional 1> and <Conditional 2>",
        "or": "<Conditional 1> or <Conditional 2>",
        "not": "not <variable name or conditional>",
    },
    "Conditionals": {
        "if Statement": "if <enter conditional here>:\n    <enter logic for if statement here>",
        "if-else Statement": "<enter conditional here>:\n    <enter logic for if statement here>\nelse:\n    <enter logic for else statement here>",
        "if-elif-else Statement": "if <enter conditional here>:\n <Enter logic here>\n elif <enter conditional here>:\n <Enter logic here>\n else:\n <Enter logic here>"
    },
    "Loops": {
        "For Loop": "for item in <Enter iterable here>:\n    <Enter logic here>",
        "While Loop": "<Enter conditional here>\n    <Enter logic here>",
        "Nested Loop": "for outer in <enter iterable here>:\n for inner in <enter iterable here>:\n if <enter conditional here>: <Enter logic here>",
        "Do-While Loop": "while True:\n <Enter logic here> \nif not <enter conditional here>:\n break",
    },
    "Functions": {
        "Define Fruitless Function": "def <Function Name>():\n    <Function logic here>",
        "Define Fruitful Function": "def <Function Name>(a, b):\n    <Function logic here>\n return <Results of Function>",
        "Function Call": "<Function name here>()",
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
    toolbox_data.Insert("Basics", "Input", "Input", [])
    toolbox_data.Insert("Logical Operators", "and", "AND", [])
    toolbox_data.Insert("Logical Operators", "or", "OR", [])
    toolbox_data.Insert("Logical Operators", "not", "NOT", [])
    toolbox_data.Insert("Conditionals", "if Statement", "if statement", [])
    toolbox_data.Insert("Conditionals", "if-else Statement", "if-else statement", [])
    toolbox_data.Insert("Conditionals", "if-elif-else Statement", "if-elif-else Statement", [])
    toolbox_data.Insert("Loops", "For Loop", "For Loop", [])
    toolbox_data.Insert("Loops", "While Loop", "While Loop", [])
    toolbox_data.Insert("Loops", "Nested Loop", "Nested Loop", [])
    toolbox_data.Insert("Loops", "Do While Loop", "Do While Loop", [])
    toolbox_data.Insert("Functions", "Define Fruitless Function", "Define Fruitless Function", [])
    toolbox_data.Insert("Functions", "Define Fruitful Function", "Define Fruitful Function", [])
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
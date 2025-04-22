import PySimpleGUI as sg

# Define toolbox commands: each category maps command names to code snippets.
toolbox_commands = {
    "Basics": {
        "Comment":"# <Enter Comment Here>",
        "print": "print('<Enter Value or Variable Name Here>')",
        "Make Variable": "<Variable Name Here> = <Value or Variable Name Here>",
        "Make multiple Variables": "<var1 name >, <var2 name>, <var3 name> = <value1>, <value2>, <value3>",
        "Input": "<Variable Name> = input('<Enter prompt for user>')",
    },
     "Math Operations": {
        "Addition": "x = 5 + 3\nprint('Result:', x)",
        "Subtraction": "x = 10 - 4\nprint('Result:', x)",
        "Multiplication": "x = 6 * 7\nprint('Result:', x)",
        "Division": "x = 20 / 4\nprint('Result:', x)",
        "Integer Division": "x = 20 // 3\nprint('Result:', x)",
        "Remainder": "x = 10 % 3\nprint('Result:', x)",
        "Exponentiation": "x = 2 ** 3\nprint('Power:', x)",
        "Increment by value": "x = 1\nx += 1\nprint(x)",
        "Decrement by value": "x = 2\nx -= 1\nprint(x)"
    },
    "Logical Operators": {
        "and": "<Conditional 1> and <Conditional 2>",
        "or": "<Conditional 1> or <Conditional 2>",
        "not": "not <variable name or conditional>",
    },
    "Conditionals": {
        "if Statement": "if <enter conditional here>:\n    <enter logic for if statement here>",
        "if-else Statement": "if <enter conditional here>:\n    <enter logic for if statement here>\nelse:\n    <enter logic for else statement here>",
        "if-elif-else Statement": "if <enter conditional here>:\n    <Enter logic here>\nelif <enter conditional here>:\n    <Enter logic here>\nelse:\n  <Enter logic here>"
    },
    "Loops": {
        "For loop": "for item in <Enter iterable here>:\n    <Enter logic here>",
        "Range based for loop with stop": "for i in range(<stop>):\n    <Enter logic here>",
        "Range based for loop with start and stop": "for i in range(<start>, <stop>):\n    <Enter logic here>",
        "Range based for loop with start, stop,and step": "for i in range(<start>, <stop>, <step>):\n    <Enter logic here>",
        "while loop": "while <Enter conditional here>:\n    <Enter logic here>",
        "Nested loop": "for outer in <enter iterable here>:\n    for inner in <enter iterable here>:\n        if <enter conditional here>:\n             <Enter logic here>",
        "do-while loop": "while True:\n    <Enter logic here> \n    if not <enter conditional here>:\n        break",
    },
    "Lists": {
        "Make a List":"<list name> = [<contents of list>]",
        "Add to a List": "<list name>.append(<element>)",
        "Remove from a List": "<list name>.remove(<element>)",
    },
    "Functions": {
        "Define Fruitless Function": "def <Function Name>(<arguments here>):\n    <Function logic here>",
        "Define Fruitful Function": "def <Function Name>(<arguments here>):\n    <Function logic here>\n    return <Results of Function>",
        "Function Call": "<Function name here>(<arguments here>)",
    },
   
}

def get_toolbox_tree():
    toolbox_data = sg.TreeData()
   
    toolbox_data = sg.TreeData()
    for category, items in toolbox_commands.items():
        toolbox_data.Insert("", category, category, [])
        for name, code in items.items():
            toolbox_data.Insert(category, name, name, [code])
    return toolbox_data

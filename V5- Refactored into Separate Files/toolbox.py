import PySimpleGUI as sg

toolbox_commands = {
    "Basics": {
        "Print": 'print("Hello, World!")',
        "Variable": 'x = 10  # Make a variable',
    },
    "Conditionals": {
        "If": 'if x > 10:\n    print("X is large")',
    },
    "Loops": {
        "ForLoop": 'for i in range(5):\n    print(i)',
    },
    "Functions": {
        "Define Function": 'def my_function():\n    print("Hello from a function!")',
    }
}

def get_toolbox_tree():
    toolbox_data = sg.TreeData()
    toolbox_data.Insert("", "Basics", "Basics", [])
    toolbox_data.Insert("", "Conditionals", "Conditionals", [])
    toolbox_data.Insert("", "Loops", "Loops", [])
    toolbox_data.Insert("", "Functions", "Functions", [])

    # Add commands under each category
    toolbox_data.Insert("Basics", "Print", "Print", [])
    toolbox_data.Insert("Basics", "Variable", "Make a Variable", [])
    toolbox_data.Insert("Conditionals", "If", "If Statement", [])
    toolbox_data.Insert("Loops", "ForLoop", "For Loop", [])

    return toolbox_data

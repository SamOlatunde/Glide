import PySimpleGUI as sg

toolbox_commands = {
    "Basics": {
        "Print": 'print("Hello, World!")',
        "Variable": 'x = 10',
    },
    "Conditionals": {
        "If": 'if x > 10:\n    print("X is large")',
    },
    "Loops": {
        "For Loop": 'for i in range(5):\n    print(i)',
        "While Loop": 'x = 0\nwhile x < 5:\n    print(x)\n    x += 1',
    },
    "Functions": {
        "Define Function": 'def my_function():\n    print("Hello from a function!")',
        "Function Call": 'my_function()',
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
    toolbox_data.Insert("Loops", "For Loop", "For Loop", [])
    toolbox_data.Insert("Loops", "While Loop", "While Loop", [])
    toolbox_data.Insert("Functions", "Define Function", "def my_function():\n    print('Hello, world!')", [])
    toolbox_data.Insert("Functions", "Function Call", "my_function()", [])
    
    return toolbox_data

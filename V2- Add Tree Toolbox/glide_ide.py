import PySimpleGUI as sg
import sys
import io
import threading
import time

# Custom input replacement for GUI
def safe_input(prompt="Enter something: "):
    return sg.popup_get_text(prompt, title="Input Required")

#Tooltip popup function 
### This was a poor attempt to make a hover option and it lowkey does not work :)
def show_tooltip(window, message, duration=2):
    win_x, win_y = window.current_location()
    win_w, win_h = window.size
    tooltip_x = win_x + 20
    tooltip_y = win_y + win_h + 10
    layout = [[sg.Text(message,
                       background_color='#FFF9C4',
                       text_color='#222222',
                       font=('Consolas', 9, 'italic'))]]
    tooltip = sg.Window('', layout, no_titlebar=True, keep_on_top=True,
                        grab_anywhere=False, location=(tooltip_x, tooltip_y),
                        finalize=True, alpha_channel=0.95)
    threading.Thread(target=lambda: (time.sleep(duration), tooltip.close()), daemon=True).start()

def run_code(code_input, output_window, var_window):
    try:
        old_stdout = sys.stdout
        sys.stdout = output_buffer = io.StringIO()
        local_vars = {"input": safe_input}
        output_window.update("")
        var_window.update("")
        exec(code_input, {}, local_vars)
        sys.stdout = old_stdout
        output_window.update(output_buffer.getvalue())
        var_display = "\n".join([f"{k}: {v}" for k, v in local_vars.items() if not k.startswith("__")])
        var_window.update(var_display if var_display else "No variables.")
    except Exception as e:
        sys.stdout = old_stdout
        output_window.update(f"Error: {e}")

# Explanations
## Needs to be updated some definitions like fruitless functions has too long of an explaination,
## OR we can take it out completely. 
explanations = {
    "Print": "Outputs text or variables to the screen.",
    "Make Variable": "Assigns a value to a variable.",
    "Declare multiple Variables": "Assigns multiple values at once.",
    "False": "Boolean value representing falsehood.",
    "True": "Boolean value representing truth.",
    "None": "Represents no value or null.",
    "and": "Logical AND operator: True if both sides are true.",
    "or": "Logical OR operator: True if at least one side is true.",
    "not": "Logical NOT operator: Inverts the boolean value.",
    "break": "Exits the nearest enclosing loop.",
    "continue": "Skips the rest of the loop and goes to the next iteration.",
    "Define Fruitless Function": "Defines a function that performs an action but returns nothing.",
    "Define Fruitful Function": "Defines a function that returns a value.",
    "Function Call": "Calls a previously defined function.",
    "Integer Division": "Divides and returns only the whole number part.",
    "Increment by value": "Increases a variable by a number.",
    "Decrement by value": "Decreases a variable by a number.",
    "open()": "Opens a file for reading or writing.",
    "with open() as": "Safely opens a file using a context manager.",
    "file.write()": "Writes content to a file.",
    "file.close()": "Closes an open file.",
    "Import pandas": "Imports the pandas library for data analysis.", ## Should Remove?
    "Import numpy": "Imports the NumPy library for numerical operations.", ## Should Remove?
    "Standard import": "Standard Python module import like math, os, etc.", ## Should Remove?
    "For Loop": "Repeats code a certain number of times using a counter variable.",
    "While Loop": "Repeats code as long as a condition is true.",
    "If Statement": "Runs code only if a condition is true.",
    "If-Else Statement": "Chooses between two code blocks based on a condition.",
    "Define Function": "Creates a function that can be called later.",
    "Function with Arguments": "Creates a function that accepts input values.",
    "Addition": "Adds two numbers.",
    "Subtraction": "Subtracts one number from another.",
    "Multiplication": "Multiplies two numbers.",
    "Division": "Divides one number by another.",
    "Modulus": "Returns the remainder of a division.",
    "Exponentiation": "Raises a number to a power.",
    "Concatenation": "Joins strings together.",
    "F-String": "Inserts variables directly into strings.",
    "Basic Input": "Asks the user to type something.",
    "Input with Conversion": "Gets user input and converts it to a number.",
}

# Toolbox Data
toolbox_data = {
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
        "If Statement": "x = 15\nif x > 10:\n    print('X is large')",
        "If-Else Statement": "x = 5\nif x > 10:\n    print('X is large')\nelse:\n    print('X is small')",
    },
    "Loops": {
        "For Loop": "for i in range(5):\n    print(i)",
        "While Loop": "x = 0\nwhile x < 5:\n    print(x)\n    x += 1",
        "break": "for i in range(10):\n    if i == 5:\n        break",
        "continue": "for i in range(10):\n    if i == 5:\n        continue",
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
        "with open() as": "with open('file.txt', 'r') as f:\n    data = f.read()",
        "file.write()": "file = open('file.txt', 'w')\nfile.write('Hello')",
        "file.close()": "file = open('file.txt', 'r')\nfile.close()",
    },
    "Module Imports": {
        "Import pandas": "import pandas as pd", ## Should Remove?
        "Import numpy": "import numpy as np", ## Should Remove?
        "Standard import": "import math" ## Should Remove?
    },
    "Input/Output": {
        "Basic Input": "name = input('Enter your name: ')\nprint('Hello,', name)",
        "Input with Conversion": "age = int(input('Enter your age: '))\nprint('In 5 years you will be', age + 5)",
    },
}


# Tree setup
tree_data = sg.TreeData()
for category, items in toolbox_data.items():
    tree_data.Insert("", category, category, [])
    for name, code in items.items():
        tree_data.Insert(category, name, name, [code])

layout = [[
    sg.Column([
        [sg.Text("Toolbox")],
        [sg.Tree(data=tree_data, headings=[], auto_size_columns=False,
                 num_rows=10, col0_width=25, key="-TOOLBOX-", enable_events=True,
                 show_expanded=False, justification='left')],
        [sg.Text("", key="-TIP-", size=(30, 2), text_color='black',
                 background_color='#FFF9C4', font=('Consolas', 9, 'italic'))],
        [sg.Checkbox("Quick Insert Mode", key="-QUICK-", enable_events=True)],
        [sg.Text("Preview:", font=('Consolas', 10, 'bold'))],
        [sg.Multiline("", size=(30, 5), key="-PREVIEW-", disabled=True,
                      background_color="#2b2b2b", text_color="#AAAAAA", font=("Consolas", 9))],
        [sg.Button("Confirm", key="-INSERT-")],
        [sg.Button("Undo Last Insert", key="-UNDO-")],
    ], expand_y=True),

    sg.Column([
        [sg.Text("Code Editor")],
        [sg.Multiline(size=(50, 18), key="-CODE-", expand_x=True, expand_y=True)],
        [sg.Button("Run Code"), sg.Button("Clear Output")],
        [sg.Text("Variables:")],
        [sg.Multiline(size=(50, 4), key="-VARS-", disabled=True, expand_x=True)],
    ], expand_x=True, expand_y=True),

    sg.Column([
        [sg.Text("Output:")],
        [sg.Multiline(size=(35, 24), key="-OUTPUT-", disabled=True, expand_x=True, expand_y=True)],
    ], expand_y=True)
]]

window = sg.Window("Glide - (Preview/Quick Insert/Undo)", layout, resizable=True)

last_insert = ""  # Track the last inserted code

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "-TOOLBOX-" and values["-TOOLBOX-"]:
        selected_item = values["-TOOLBOX-"][0]
        for category, items in toolbox_data.items():
            if selected_item in items:
                code_snippet = items[selected_item]
                if values["-QUICK-"]:
                    last_insert = code_snippet
                    window["-CODE-"].update(values["-CODE-"] + "\n" + code_snippet)
                else:
                    window["-PREVIEW-"].update(code_snippet)
                if selected_item in explanations:
                    window["-TIP-"].update(explanations[selected_item])
                break

    elif event == "-INSERT-":
        preview_code = values["-PREVIEW-"]
        current_code = values["-CODE-"]
        last_insert = preview_code
        window["-CODE-"].update(current_code + "\n" + preview_code)
        window["-PREVIEW-"].update("")

    elif event == "-UNDO-" and last_insert:
        current_code = values["-CODE-"]
        if last_insert in current_code:
            new_code = current_code.rsplit(last_insert, 1)[0]
            window["-CODE-"].update(new_code.strip())
            last_insert = ""

    elif event == "Run Code":
        run_code(values["-CODE-"], window["-OUTPUT-"], window["-VARS-"])

    elif event == "Clear Output":
        window["-OUTPUT-"].update("")
        window["-VARS-"].update("")

window.close()

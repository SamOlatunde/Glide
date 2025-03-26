import PySimpleGUI as sg
import sys
import io

# Function to execute the code and capture variables
def run_code(code_input, output_window, var_window):
    try:
        old_stdout = sys.stdout
        sys.stdout = output_buffer = io.StringIO()

        local_vars = {}
        exec(code_input, {}, local_vars)

        sys.stdout = old_stdout
        output_window.update(output_buffer.getvalue())

        var_display = "\n".join([f"{k}: {v}" for k, v in local_vars.items()])
        var_window.update(var_display if var_display else "No variables.")

    except Exception as e:
        sys.stdout = old_stdout
        output_window.update(f"Error: {e}")

# Define the toolbox structure
toolbox_data = {
    "Loops": {
        "For Loop": 'for i in range(5):\n    print(i)',
        "While Loop": 'x = 0\nwhile x < 5:\n    print(x)\n    x += 1',
    },
    "Conditionals": {
        "If Statement": 'if x > 10:\n    print("X is large")',
        "If-Else Statement": 'if x > 10:\n    print("X is large")\nelse:\n    print("X is small")',
    },
    "Functions": {
        "Define Function": 'def my_function():\n    print("Hello from a function!")',
        "Function with Arguments": 'def greet(name):\n    print(f"Hello, {name}!")',
    }
}

# Convert toolbox structure into tree data
tree_data = sg.TreeData()
for category, items in toolbox_data.items():
    tree_data.Insert("", category, category, [])  # Category (parent)
    for name, code in items.items():
        tree_data.Insert(category, name, name, [code])  # Command (child)

# GUI Layout
layout = [
    [
        # Toolbox (Collapsible)
        sg.Column([
            [sg.Text("Toolbox", font=("Arial", 12, "bold"))],
            [sg.Tree(data=tree_data, headings=[], auto_size_columns=False,
                     num_rows=10, col0_width=20, key="-TOOLBOX-", enable_events=True,
                     show_expanded=False, justification='left')],
        ], element_justification='left', expand_y=True),

        # Code Editor + Variables
        sg.Column([
            [sg.Text("Glide - Hybrid IDE", font=("Arial", 14, "bold"))],
            [sg.Text("Code Editor")],
            [sg.Multiline(size=(40, 15), key="-CODE-", expand_x=True, expand_y=True)],
            [sg.Button("Run Code"), sg.Button("Clear Output")],
            [sg.Text("Variables:")],
            [sg.Multiline(size=(40, 4), key="-VARS-", disabled=True, expand_x=True)],
        ], expand_x=True, expand_y=True),

        # Output Panel
        sg.Column([
            [sg.Text("Output:")],
            [sg.Multiline(size=(30, 15), key="-OUTPUT-", disabled=True, expand_x=True, expand_y=True)],
        ], expand_y=True),
    ]
]

# Create Window
window = sg.Window("Glide - Hybrid IDE", layout, resizable=True)

# Event Loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Run Code":
        run_code(values["-CODE-"], window["-OUTPUT-"], window["-VARS-"])

    if event == "Clear Output":
        window["-OUTPUT-"].update("")
        window["-VARS-"].update("")

    # When a toolbox item is selected, insert the corresponding code
    if event == "-TOOLBOX-" and values["-TOOLBOX-"]:
        selected_item = values["-TOOLBOX-"][0]
        for category, items in toolbox_data.items():
            if selected_item in items:
                window["-CODE-"].update(values["-CODE-"] + "\n" + items[selected_item])

window.close()

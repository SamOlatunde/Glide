import PySimpleGUI as sg
import sys
import io

# Function to execute the code and capture variables
def run_code(code_input, output_window, var_window):
    try:
        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        sys.stdout = output_buffer = io.StringIO()

        # Execute the code
        local_vars = {}
        exec(code_input, {}, local_vars)

        # Restore stdout
        sys.stdout = old_stdout

        # Display output
        output_window.update(output_buffer.getvalue())

        # Display variables
        var_display = "\n".join([f"{k}: {v}" for k, v in local_vars.items()])
        var_window.update(var_display if var_display else "No variables.")

    except Exception as e:
        sys.stdout = old_stdout
        output_window.update(f"Error: {e}")

# Toolbox with collapsible sections
toolbox_commands = {
    "Loops": {
        "For Loop": 'for i in range(5):\n    print(i)',
        "While Loop": 'x = 0\nwhile x < 5:\n    print(x)\n    x += 1'
    },
    "Conditionals": {
        "If Statement": 'if x > 10:\n    print("X is large")',
        "If-Else Statement": 'if x > 10:\n    print("X is large")\nelse:\n    print("X is small")'
    },
    "Functions": {
        "Define Function": 'def my_function():\n    print("Hello from a function")',
        "Function Call": 'my_function()'
    },
    "Basics": {
        "Print": 'print("Hello, world!")',
        "Input": ['name = input("Enter your name: ")\nprint("Hello, " + name)']  # FIX: Wrapped in a list
    }
}

# Convert toolbox structure to PySimpleGUI Tree format
toolbox_tree_data = sg.TreeData()
for category, commands in toolbox_commands.items():
    toolbox_tree_data.Insert("", category, category, [])
    for cmd_name, cmd_code in commands.items():
        toolbox_tree_data.Insert(category, cmd_name, cmd_name, [cmd_code])  # FIX: Values must be a list

# Toolbox Layout inside a Frame
toolbox_pane = sg.Column([
    [sg.Text("Toolbox", font=("Arial", 12, "bold"))],
    [sg.Tree(data=toolbox_tree_data, headings=[], select_mode=sg.TABLE_SELECT_MODE_BROWSE,
             key="-TOOLBOX-", enable_events=True, show_expanded=False, col0_width=20, expand_x=True, expand_y=True)],
], expand_x=True, expand_y=True)

# Main GUI Layout with a resizable Pane
layout = [
    [
        sg.Pane(
            [
                toolbox_pane,
                sg.Column([  # Middle column for workspace
                    [sg.Text("Code Editor")],
                    [sg.Multiline(size=(None, 18), key="-CODE-", expand_x=True, expand_y=True)],
                    [sg.Button("Run Code"), sg.Button("Clear Output")],
                    [sg.Text("Variables:")],
                    [sg.Multiline(size=(None, 5), key="-VARS-", disabled=True, expand_x=True)]
                ], expand_x=True, expand_y=True),
                sg.Column([  # Right column for output
                    [sg.Text("Output:")],
                    [sg.Multiline(size=(None, 10), key="-OUTPUT-", disabled=True, expand_x=True, expand_y=True)]
                ], expand_x=True, expand_y=True)
            ],
            orientation="h", handle_size=10, expand_x=True, expand_y=True
        )
    ]
]

# Create Window
window = sg.Window("Glide - Hybrid IDE", layout, resizable=True, finalize=True)

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

    if event == "-TOOLBOX-" and values["-TOOLBOX-"]:
        selected_item = values["-TOOLBOX-"][0]
        if selected_item in toolbox_tree_data.tree_dict and toolbox_tree_data.tree_dict[selected_item].values:
            new_snippet = f"# Insert a comment here\n{toolbox_tree_data.tree_dict[selected_item].values[0]}\n\n"
            current_code = values["-CODE-"].strip()
            updated_code = (current_code + "\n\n" + new_snippet).strip()
            window["-CODE-"].update(updated_code)

window.close()

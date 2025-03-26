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

# Predefined toolbox commands
toolbox_commands = {
    "Print": 'print("Hello, world!")',
    "For Loop": 'for i in range(5):\n    print(i)',
    "If Statement": 'if x > 10:\n    print("X is large")',
}

# GUI Layout
layout = [
    [
        # Toolbox Panel (Left)
        sg.Column([
            [sg.Text("Glide - Hybrid IDE", font=("Arial", 14, "bold"))],
            [sg.Text("Toolbox")],
            [sg.Listbox(values=list(toolbox_commands.keys()), size=(20, 6), key="-TOOLBOX-", enable_events=True)],
        ], element_justification='left', expand_y=True),

        # Middle Panel (Code Editor + Variables)
        sg.Column([
            [sg.Text("Code Editor")],
            [sg.Multiline(size=(40, 15), key="-CODE-", expand_x=True, expand_y=True)],
            [sg.Button("Run Code"), sg.Button("Clear Output")],
            [sg.Text("Variables:")],
            [sg.Multiline(size=(40, 4), key="-VARS-", disabled=True, expand_x=True)],
        ], expand_x=True, expand_y=True),

        # Output Panel (Right)
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

    if event == "-TOOLBOX-" and values["-TOOLBOX-"]:
        selected_command = values["-TOOLBOX-"][0]
        window["-CODE-"].update(values["-CODE-"] + "\n" + toolbox_commands[selected_command])

window.close()

from toolbox import toolbox_commands
from execution import run_code

def handle_events(event, values, window):
    if event == "Run Code":
        code_text = window.TKEditor.get("1.0", "end-1c")
        run_code(code_text, window["-OUTPUT-"], window["-VARS-"])

    if event == "Clear Output":
        window["-OUTPUT-"].update("")
        window["-VARS-"].update("")

    if event == "-TOOLBOX-" and values["-TOOLBOX-"]:
        selected_item = values["-TOOLBOX-"][0]
        for category, commands in toolbox_commands.items():
            if selected_item in commands:
                new_code = "# Insert a comment here\n" + commands[selected_item]
                current_code = window.TKEditor.get("1.0", "end-1c")
                if current_code.strip() == "":
                    updated_code = new_code
                else:
                    updated_code = current_code.rstrip() + "\n\n" + new_code
                window.TKEditor.delete("1.0", "end")
                window.TKEditor.insert("1.0", updated_code)
                break
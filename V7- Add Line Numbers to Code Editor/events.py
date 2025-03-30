from toolbox import toolbox_commands
from execution import run_code

def handle_events(event, values, window):
    if event == "Run Code":
        run_code(window.TKEditor.text.get("1.0", "end-1c"), window["-OUTPUT-"], window["-VARS-"])

    if event == "Reset":
        window["-OUTPUT-"].update("")
        window["-VARS-"].update("")
        window.TKEditor.text.delete("1.0", "end")

    if event == "-TOOLBOX-" and values["-TOOLBOX-"]:
        selected_item = values["-TOOLBOX-"][0]
        for category, items in toolbox_commands.items():
            if selected_item in items:
                new_code = f"# Insert a comment here\n{items[selected_item]}\n"
                current_code = window.TKEditor.text.get("1.0", "end-1c").rstrip()
                updated_code = (current_code + "\n\n" + new_code).strip()
                window.TKEditor.text.delete("1.0", "end")
                window.TKEditor.text.insert("1.0", updated_code)
                window.TKEditor.highlight_syntax()
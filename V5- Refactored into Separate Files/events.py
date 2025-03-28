from execution import run_code
from toolbox import toolbox_commands  # Import the toolbox data from the toolbox module

def handle_events(event, values, window):
    # Handling "Run Code" event
    if event == "Run Code":
        run_code(values["-CODE-"], window["-OUTPUT-"], window["-VARS-"])

    # Handling "Clear Output" event
    if event == "Clear Output":
        window["-OUTPUT-"].update("")
        window["-VARS-"].update("")

    # Handling toolbox item selection
    if event == "-TOOLBOX-" and values["-TOOLBOX-"]:
        selected_item = values["-TOOLBOX-"][0]
        for category, items in toolbox_commands.items():
            if selected_item in items:
                # Ensure a blank line is added after the snippet
                new_snippet = f"# Insert a comment here\n{items[selected_item]}\n\n"
                current_code = values["-CODE-"].rstrip()  # Trim trailing spaces/newlines
                updated_code = (current_code + "\n\n" + new_snippet).strip()  # Ensure spacing
                window["-CODE-"].update(updated_code)
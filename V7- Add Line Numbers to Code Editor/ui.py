import PySimpleGUI as sg
from toolbox import get_toolbox_tree

def create_layout():
    toolbox_tree = get_toolbox_tree()

    # Toolbox pane
    toolbox_pane = sg.Column([
        [sg.Text("Toolbox", font=("Arial", 12, "bold"))],
        [sg.Tree(data=toolbox_tree, headings=[], select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                 key="-TOOLBOX-", enable_events=True, show_expanded=False,
                 col0_width=20, expand_x=True, expand_y=True)]
    ], expand_x=True, expand_y=True)

    # Code editor (Canvas) - Add placeholder functionality
    code_canvas = sg.Canvas(key="-CODE_CANVAS-", size=(600, 400))

    # Define the placeholder text for Multiline elements
    placeholder_vars = "<Insert comments here>"
    placeholder_output = "<Insert comments here>"

    # Variable display (with placeholder text)
    var_display = sg.Multiline(size=(40, 4), key="-VARS-", disabled=True, expand_x=True,
                                default_text=placeholder_vars)  # Add placeholder

    # Output panel (with placeholder text)
    output_panel = sg.Multiline(size=(30, 15), key="-OUTPUT-", disabled=True, expand_x=True, expand_y=True,
                                 default_text=placeholder_output)  # Add placeholder

    layout = [
        [sg.Pane([  # Split the layout horizontally
            toolbox_pane,  # Toolbox panel
            sg.Column([  # Editor and variables column
                [sg.Text("Code Editor")],
                [code_canvas],  # Code canvas
                [sg.Button("Run Code"), sg.Button("Reset")],
                [sg.Text("Variables:")],
                [var_display]  # Variable display with placeholder
            ], expand_x=True, expand_y=True),
            sg.Column([  # Output column
                [sg.Text("Output:")],
                [output_panel]  # Output panel with placeholder
            ], expand_x=True, expand_y=True)
        ], orientation="h", handle_size=10, expand_x=True, expand_y=True)]
    ]

    return layout

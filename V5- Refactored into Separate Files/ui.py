import PySimpleGUI as sg
from toolbox import get_toolbox_tree  # Import toolbox function

# Create the layout with adjustable horizontal sizing
def create_layout():
    toolbox_tree = get_toolbox_tree()  # Get the toolbox tree data

    # Toolbox Layout inside a Frame
    toolbox_pane = sg.Column([
        [sg.Text("Toolbox")],
        [sg.Tree(data=toolbox_tree, headings=[], select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                 key="-TOOLBOX-", enable_events=True, show_expanded=False, col0_width=20, expand_x=True, expand_y=True)],
    ], expand_x=True, expand_y=True)

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
    return layout
import PySimpleGUI as sg
from toolbox import get_toolbox_tree

def create_layout():
    toolbox_tree = get_toolbox_tree()

    toolbox_column = sg.Column([
        [sg.Text("Toolbox", font=("Arial", 12, "bold"))],
        [sg.Tree(data=toolbox_tree, headings=[], auto_size_columns=False, select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                 key="-TOOLBOX-", enable_events=True, show_expanded=False)],
    ], expand_x=True, expand_y=True)

    workspace_column = sg.Column([
        [sg.Text("Code Editor")],
        [sg.Multiline(size=(50, 15), key="-CODE-", expand_x=True, expand_y=True)],
        [sg.Button("Run Code"), sg.Button("Clear Output")],
        [sg.Text("Variables:")],
        [sg.Multiline(size=(50, 4), key="-VARS-", disabled=True, expand_x=True)],
    ], expand_x=True, expand_y=True)

    output_column = sg.Column([
        [sg.Text("Output:")],
        [sg.Multiline(size=(50, 6), key="-OUTPUT-", disabled=True, expand_x=True, expand_y=True)],
    ], expand_x=True, expand_y=True)

    layout = [[toolbox_column, workspace_column, output_column]]
    return layout
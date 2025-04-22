import PySimpleGUI as sg
from ui import create_layout
from events import handle_events
from code_editor import create_code_editor
placeholder = "Insert a comment here"

def main():
   layout = create_layout()
   window = sg.Window("Glide - Hybrid IDE", layout, resizable=True, finalize=True)

   # Create and attach the custom CodeEditor into the Canvas
   if "-CODE_CANVAS-" in window.AllKeysDict:
       editor = create_code_editor(window["-CODE_CANVAS-"])
       window.TKEditor = editor  # This makes it available to events.py

   while True:
       event, values = window.read() # input values of each event in an iteration is read
       if event == sg.WINDOW_CLOSED: # Close window when user exits 
           break

       if event == "-CODE-" and values["-CODE-"] == placeholder:
           window["-CODE-"].update("")  # Clear the placeholder if code editor is focused

       if event in ("Run Code", "Clear Output") and not values["-CODE-"].strip():
           window["-CODE-"].update(placeholder)  # Restore the placeholder if editor is left empty

       handle_events(event, values, window)
   window.close() #close app window after loop ends
if __name__ == "__main__":
   main()

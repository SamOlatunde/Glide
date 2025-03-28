import PySimpleGUI as sg
from ui import create_layout
from events import handle_events

def main():
    sg.theme("DarkBlue")  # Set theme

    layout = create_layout()
    window = sg.Window("Glide - Hybrid IDE", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        handle_events(event, values, window)

    window.close()

if __name__ == "__main__":
    main()
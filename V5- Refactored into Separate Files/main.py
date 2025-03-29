import PySimpleGUI as sg
from ui import create_layout
from events import handle_events

def main():
    sg.theme("DarkBlue")  # Set theme
    '''
        Note- these are some other themes available (I personally did not care for most of them):
        We can also set custom colors using hex values and just skip a theme altogether.
            DarkBlue- A dark theme with blue accents.
            DarkGrey- A darker theme with grey tones.
            LightGrey- A light theme with grey accents.
            Reddit- A theme inspired by Reddit's color scheme.
            BlueMono- A theme with blue and black tones, good for monochrome designs.
            GreenMono- A green-based theme, also monochrome.
            SystemDefault- The default system theme (based on your OS).
            Topanga- A theme with a mix of purple and yellow hues.
            SandyBeach- Light tan with a relaxed, beachy feel.
            BrightColors- A theme with bold, bright colors.
    '''

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

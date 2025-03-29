import tkinter as tk
import keyword
import builtins

class CodeEditor(tk.Text):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(
            font=("Courier", 12),
            wrap="none",
            undo=True,
            bg="white",
            fg="black",
            insertbackground="black"
        )

        self.tag_configure("keyword", foreground="#800080")     # Purple
        self.tag_configure("builtin", foreground="#a87d20")     # Brownish-Orange
        self.tag_configure("comment", foreground="#228B22")     # Green
        self.tag_configure("string", foreground="#a42107")      # Brownish-Red
        self.tag_configure("primitive", foreground="blue")      # Blue

        self.bind("<KeyRelease>", self.on_key_release)
        self.bind("<<Paste>>", self.on_key_release)

        self.highlight_syntax()

    def on_key_release(self, event=None):
        self.after_idle(self.highlight_syntax)

    def highlight_syntax(self):
        self.tag_remove("keyword", "1.0", "end")
        self.tag_remove("builtin", "1.0", "end")
        self.tag_remove("comment", "1.0", "end")
        self.tag_remove("string", "1.0", "end")
        self.tag_remove("primitive", "1.0", "end")

        content = self.get("1.0", "end-1c")
        tokens = content.replace("(", " ").replace(")", " ").replace(":", " ").split()
        builtin_names = set(dir(builtins))

        # Highlight comments
        start_index = "1.0"
        while True:
            pos = self.search("#", start_index, stopindex="end")
            if not pos:
                break
            line_end = self.search("\n", pos, stopindex="end")
            if not line_end:
                line_end = "end-1c"
            self.tag_add("comment", pos, line_end)
            start_index = line_end

        # Highlight strings: double quotes
        start_index = "1.0"
        while True:
            pos = self.search("\"", start_index, stopindex="end")
            if not pos:
                break
            end_pos = self.search("\"", f"{pos}+1c", stopindex="end")
            if not end_pos:
                break
            end_index = f"{end_pos}+1c"
            self.tag_add("string", pos, end_index)
            start_index = end_index

        # Highlight strings: single quotes
        start_index = "1.0"
        while True:
            pos = self.search("'", start_index, stopindex="end")
            if not pos:
                break
            end_pos = self.search("'", f"{pos}+1c", stopindex="end")
            if not end_pos:
                break
            end_index = f"{end_pos}+1c"
            self.tag_add("string", pos, end_index)
            start_index = end_index

        # Highlight primitive constants
        for const in ["True", "False", "None"]:
            start_index = "1.0"
            while True:
                pos = self.search(const, start_index, stopindex="end")
                if not pos:
                    break
                end_index = f"{pos}+{len(const)}c"
                matched = self.get(pos, end_index)
                if matched == const:
                    self.tag_add("primitive", pos, end_index)
                start_index = end_index

        # Highlight numbers
        start_index = "1.0"
        while True:
            pos = self.search(r'\d+', start_index, stopindex="end", regexp=True)
            if not pos:
                break
            end_index = self.index(f"{pos} wordend")
            self.tag_add("primitive", pos, end_index)
            start_index = end_index

        # Highlight keywords and built-ins
        for token in set(tokens):
            start_index = "1.0"
            while True:
                pos = self.search(token, start_index, stopindex="end")
                if not pos:
                    break
                end_index = f"{pos}+{len(token)}c"
                matched = self.get(pos, end_index)

                if matched == token:
                    if token in keyword.kwlist:
                        self.tag_add("keyword", pos, end_index)
                    elif token in builtin_names:
                        self.tag_add("builtin", pos, end_index)

                start_index = end_index

def create_code_editor(canvas):
    tk_canvas = canvas.TKCanvas
    editor = CodeEditor(tk_canvas.master, height=20, width=80)
    tk_canvas.create_window((0, 0), window=editor, anchor="nw")
    return editor
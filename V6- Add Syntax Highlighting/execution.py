import sys
import io

def run_code(code_input, output_window, var_window):
    try:
        old_stdout = sys.stdout
        sys.stdout = output_buffer = io.StringIO()

        local_vars = {}
        exec(code_input, {}, local_vars)

        sys.stdout = old_stdout
        output_window.update(output_buffer.getvalue())

        var_display = "\n".join([f"{k}: {v}" for k, v in local_vars.items()])
        var_window.update(var_display if var_display else "No variables.")
    except Exception as e:
        sys.stdout = old_stdout
        output_window.update(f"Error: {e}")
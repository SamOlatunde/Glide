import sys
import io

def run_code(code_input, output_window, var_window):
    try:
        old_stdout = sys.stdout
        sys.stdout = output_buffer = io.StringIO()

        local_vars = {}
        exec(code_input, {}, local_vars)

        sys.stdout = old_stdout

        # Get the current code from the code editor and strip any trailing spaces/newlines
        current_code = code_input.rstrip()

        # Insert comment and add a blank line after the code snippet
        new_snippet = f"# Insert a comment here\n{current_code}\n\n"  # Ensures blank line after each snippet

        # Update the code in the editor
        updated_code = (current_code + "\n" + new_snippet).strip()  # Make sure spacing between code is as expected
        
        # Update the code editor with the new snippet
        output_window.update(updated_code)

        # Display the output from the executed code
        output_text = output_buffer.getvalue().strip()  # Clean any extra spaces or newlines from the output
        output_window.update(output_text)

        # Display variables
        var_display = "\n".join([f"{k}: {v}" for k, v in local_vars.items()])
        var_window.update(var_display.strip() if var_display else "No variables.")

    except Exception as e:
        sys.stdout = old_stdout
        output_window.update(f"Error: {e}")

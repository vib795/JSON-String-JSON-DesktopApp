import tkinter as tk
from tkinter import messagebox
import json

def convert_to_json():
    input_string = input_text.get("1.0", tk.END).strip()

    try:
        input_string = input_string.encode().decode('unicode_escape')
        # Check if the string starts and ends with quotes and remove them
        if input_string.startswith('"') and input_string.endswith('"'):
            input_string = input_string[1:-1]

        # Replace escaped double quotes with actual double quotes
        input_string = input_string.replace('\\"', '"')

        # Convert string to JSON
        json_object = json.loads(input_string)

        # Format JSON for display
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, json.dumps(json_object, indent=4, sort_keys=False))
        output_text.config(state=tk.DISABLED)
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid JSON format")


def reverse_convert_json():
    input_json = input_text.get("1.0", tk.END).strip()
    try:
        # Convert the input string to a JSON object to ensure it's valid JSON
        json_object = json.loads(input_json)
        
        # Convert the JSON object back to a string with special escaping
        json_string = json.dumps(json_object)
        escaped_json_string = json_string.replace('"', '\\"')
        
        # Wrap the escaped string in additional quotes
        final_string = f'"{escaped_json_string}"'
        
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, final_string)
        output_text.config(state=tk.DISABLED)
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid JSON format")

# Set up the main window
root = tk.Tk()
root.title("JSON Formatter")

# Create input text area
input_label = tk.Label(root, text="Input:")
input_label.pack()
input_text = tk.Text(root, height=20, width=60)
input_text.pack(padx=10, pady=(0, 10))

# Create buttons
convert_button = tk.Button(root, text="Convert to JSON", command=convert_to_json)
convert_button.pack(side=tk.LEFT, padx=(10, 5), pady=10)
reverse_convert_button = tk.Button(root, text="Reverse Convert", command=reverse_convert_json)
reverse_convert_button.pack(side=tk.RIGHT, padx=(5, 10), pady=10)

# Create output text area
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text = tk.Text(root, height=20, width=60)
output_text.pack(padx=10, pady=(0, 10))
output_text.config(state=tk.DISABLED)


root.mainloop()

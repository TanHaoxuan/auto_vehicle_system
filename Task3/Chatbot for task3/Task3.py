import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from gpt4all import GPT4All

# Available models (You can modify this list)
MODEL_OPTIONS = [
    "orca-mini-3b-gguf2-q4_0.gguf",
    "mistral-7b-instruct-v0.1.Q4_K.gguf",
    "llama-2-7b-chat.ggmlv3.q4_0"
]

# Initialize the main application window
root = tk.Tk()
root.title("LLM Interface")
root.geometry("700x500")
root.configure(bg="#333333")  # Dark background

# Function to generate a response from GPT4All
def generate_response():
    user_text = input_text.get("1.0", tk.END).strip()
    if user_text:
        selected_model = model_var.get()
        model = GPT4All(selected_model, device="cpu")  # Running on CPU
        response = model.generate(user_text, max_tokens=100000)
        
        output_text.insert(tk.END, f"You: {user_text}\n", "user")
        output_text.insert(tk.END, f"Bot: {response}\n\n", "bot")
        output_text.see(tk.END)

# Function to clear input text
def clear_input():
    input_text.delete("1.0", tk.END)

# Function to clear output text
def clear_output():
    output_text.delete("1.0", tk.END)

# Function to exit the application
def exit_app():
    root.destroy()

# Title Label
title_label = tk.Label(root, text="LLM Interface", font=("Helvetica", 16, "bold"), bg="#333333", fg="white")
title_label.pack(pady=10)

# Dropdown for model selection
model_var = tk.StringVar(value=MODEL_OPTIONS[0])
model_dropdown = ttk.Combobox(root, textvariable=model_var, values=MODEL_OPTIONS, state="readonly")
model_dropdown.pack(pady=5)

# Input Textbox
input_label = tk.Label(root, text="Send a Message:", font=("Helvetica", 12), bg="#333333", fg="white")
input_label.pack()
input_text = ScrolledText(root, wrap=tk.WORD, width=60, height=5, bg="#222222", fg="white", insertbackground="white")
input_text.pack(pady=5)

# Generate Response Button
generate_button = tk.Button(root, text="Generate Response", command=generate_response, bg="#555555", fg="white", font=("Helvetica", 12))
generate_button.pack(pady=5)

# Output Textbox
output_text = ScrolledText(root, wrap=tk.WORD, width=60, height=10, bg="#222222", fg="white", insertbackground="white")
output_text.pack(pady=5)

# Tag Configurations for Coloring Output
output_text.tag_configure("user", foreground="#00FF00")  # Green for user text
output_text.tag_configure("bot", foreground="#FFAA00")  # Orange for bot response

# Control Buttons (Clear Input, Clear Output, Exit)
button_frame = tk.Frame(root, bg="#333333")
button_frame.pack(pady=10)

clear_input_button = tk.Button(button_frame, text="Clear Input", command=clear_input, bg="#555555", fg="white", font=("Helvetica", 10))
clear_input_button.grid(row=0, column=0, padx=10)

clear_output_button = tk.Button(button_frame, text="Clear Output", command=clear_output, bg="#555555", fg="white", font=("Helvetica", 10))
clear_output_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="#AA0000", fg="white", font=("Helvetica", 10, "bold"))
exit_button.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()

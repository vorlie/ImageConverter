import tkinter as tk, ctypes, os
from tkinter import filedialog
from PIL import Image

icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")

def display_notification(title, message, duration=5):
    duration_seconds = int(duration * 1000)
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x40000)

def convert_image(input_file_path, output_format):
    try:
        output_folder = os.path.dirname(input_file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))
        output_file_path = os.path.join(output_folder, f"{file_name}_converted.{output_format}")
        im = Image.open(input_file_path)
        im.save(output_file_path, output_format.upper())
        display_notification("Conversion Complete", f"File converted successfully.\nOutput: {output_file_path.replace('/', os.path.sep)}")
    except Exception as e:
        display_notification("Error", f"Error converting file: {e}")

def select_file_and_convert():
    global file_path
    file_path = filedialog.askopenfilename(title="Select file",
                                           filetypes=(("All files", "*.*"), ("WebP files", "*.webp"), ("PNG files", "*.png"), ("JPG files", "*.jpg")))
    if file_path:
        if not hasattr(root, "conversion_menu"):
            create_conversion_widgets()
        display_selected_file(file_path)

def create_conversion_widgets():
    global conversion_var, conversion_menu, convert_button
    conversion_var.set("Select conversion format")
    conversion_choices = ["JPEG", "WebP", "PNG","GIF","TIFF","BPM"]
    conversion_menu = tk.OptionMenu(
        root, 
        conversion_var, 
        *conversion_choices)
    conversion_menu.pack(anchor="w", pady=2, padx=10)
    convert_button = tk.Button(
        root, 
        text="Convert", 
        command=convert_file,
        bg=colors["accent"], 
        fg=colors["fg"],
        border=0,
        borderwidth=0,
        activebackground=colors["active_accent"])
    convert_button.pack(anchor="w", pady=2, padx=10)

def display_selected_file(file_path):
    filename = os.path.basename(file_path)
    selected_file_label.config(text=f"Selected File: {filename}")

def convert_file():
    conversion_choice = conversion_var.get()
    if not conversion_choice:
        display_notification("Error", "Please select a file format.")
        return
    format_mapping = {
        "JPEG": "jpeg",
        "WebP": "webp",
        "PNG": "png",
        "GIF": "gif",
        "TIFF": "tiff",
        "BMP": "bmp"
    }
    if conversion_choice in format_mapping:
        output_format = format_mapping[conversion_choice]
        convert_image(file_path, output_format)
    else:
        display_notification("Error", "Invalid conversion choice. Please select a conversion format.")

colors = {
    "bg": "#303030",
    "fg": "#FFFFFF",
    "fg2": "#000000",
    "accent": "#C81443",
    "active_accent": "#FF4D7B"}
root = tk.Tk()
root.iconbitmap(icon_path)
root.geometry("500x140")
root.resizable("true", "false")
root.title("Image Format Converter")
root.tk_setPalette(
    background=colors["bg"], 
    foreground=colors["fg"], 
    activeBackground=colors["bg"], 
    activeForeground=colors["fg2"])

conversion_var = tk.StringVar()
file_path = None

select_button = tk.Button(
    root, 
    text="Select File", 
    command=select_file_and_convert, 
    bg=colors["accent"], 
    fg=colors["fg"],
    border=0,
    borderwidth=0,
    activebackground=colors["active_accent"])
select_button.pack(anchor="w", pady=10, padx=10)

selected_file_label = tk.Label(root, text="")
selected_file_label.pack(anchor="w", pady=2, padx=10)

root.mainloop()
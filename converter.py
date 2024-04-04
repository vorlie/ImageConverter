import tkinter as tk, os, ctypes
from tkinter import filedialog
from PIL import Image

icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")

def display_notification(title, message, duration=5):
    duration_seconds = int(duration * 1000)
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x40000)

def convert_webp_to_png(input_file_path):
    try:
        output_folder = os.path.dirname(input_file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))
        png_file_path = os.path.join(output_folder, f"{file_name}_converted.png")
        im = Image.open(input_file_path).convert("RGB")
        im.save(png_file_path, "PNG")
        display_notification("Conversion Complete", f"WebP to PNG conversion successful.\nOutput: {png_file_path.replace('/', os.path.sep)}")
    except Exception as e:
        display_notification("Error", f"Error converting WebP to PNG: {e}")
        
def convert_png_to_webp(input_file_path):
    try:
        output_folder = os.path.dirname(input_file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))
        webp_file_path = os.path.join(output_folder, f"{file_name}_converted.webp")
        im = Image.open(input_file_path)
        im.save(webp_file_path, "WEBP")
        display_notification("Conversion Complete", f"PNG to WebP conversion successful.\nOutput: {webp_file_path.replace('/', os.path.sep)}")
    except Exception as e:
        display_notification("Error", f"Error converting PNG to WebP: {e}")

def convert_jpg_to_png(input_file_path):
    try:
        output_folder = os.path.dirname(input_file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))
        png_file_path = os.path.join(output_folder, f"{file_name}_converted.png")
        img = Image.open(input_file_path)
        img.save(png_file_path, "PNG")
        display_notification("Conversion Complete", f"JPG file converted to PNG successfully.\nOutput: {png_file_path.replace('/', os.path.sep)}")
    except Exception as e:
        display_notification("Error", f"Error converting JPG to PNG: {e}")

def convert_png_to_jpg(input_file_path):
    try:
        output_folder = os.path.dirname(input_file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))
        jpg_file_path = os.path.join(output_folder, f"{file_name}_converted.jpg")
        img = Image.open(input_file_path)
        img.save(jpg_file_path, "JPEG")
        display_notification("Conversion Complete", f"PNG file converted to JPEG successfully.\nOutput: {jpg_file_path.replace('/', os.path.sep)}")
    except Exception as e:
        display_notification("Error", f"Error converting PNG to JPG: {e}")

def convert_webp_to_jpg(input_file_path):
    try:
        output_folder = os.path.dirname(input_file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))
        jpg_file_path = os.path.join(output_folder, f"{file_name}_converted.jpg")
        img = Image.open(input_file_path)
        img.save(jpg_file_path, "JPEG")
        display_notification("Conversion Complete", f"WebP file converted to JPEG successfully.\nOutput: {jpg_file_path.replace('/', os.path.sep)}")
    except Exception as e:
        display_notification("Error", f"Error converting WebP to JPEG: {e}")

def convert_jpg_to_webp(input_file_path):
    try:
        output_folder = os.path.dirname(input_file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))
        webp_file_path = os.path.join(output_folder, f"{file_name}_converted.webp")
        img = Image.open(input_file_path)
        img.save(webp_file_path, "WEBP")
        display_notification("Conversion Complete", f"JPEG file converted to WebP successfully.\nOutput: {webp_file_path.replace('/', os.path.sep)}")
    except Exception as e:
        display_notification("Error", f"Error converting JPEG to WebP: {e}")

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
    conversion_choices = ["WebP to JPG", "PNG to JPG", "JPG to WebP", "JPG to PNG", "PNG to WebP", "WebP to PNG"]
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
    if conversion_choice == "WebP to JPG":
        convert_webp_to_jpg(file_path)
    elif conversion_choice == "PNG to JPG":
        convert_png_to_jpg(file_path)
    elif conversion_choice == "JPG to PNG":
        convert_jpg_to_png(file_path)
    elif conversion_choice == "JPG to WebP":
        convert_jpg_to_webp(file_path)
    elif conversion_choice == "PNG to WebP":
        convert_png_to_webp(file_path)
    elif conversion_choice == "WebP to PNG":
        convert_webp_to_png(file_path)
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
root.title("File Format Converter")
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
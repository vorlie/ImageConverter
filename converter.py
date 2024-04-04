import tkinter as tk, sys, os, ctypes
from tkinter import filedialog
from PIL import Image

icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")

def display_notification(title, message, duration=5):
    duration_seconds = int(duration * 1000) 
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x40000) 
    
def convert_webp_to_png(file_path):
    output_folder = os.path.dirname(file_path)
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    png_file_path = os.path.join(output_folder, f"{file_name}_converted.png")
    im = Image.open(file_path).convert("RGB")
    im.save(png_file_path, "PNG")
    
    display_notification("Conversion Complete", f"WebP to PNG conversion successful. Output: {png_file_path}")

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    convert_webp_to_png(file_path)
else:
    root = tk.Tk()
    root.iconbitmap(icon_path)
    root.geometry("300x200")
    root.resizable(False, False)
    root.title("WebP to PNG Converter")

    def select_file_and_convert():
        webp_file_path = filedialog.askopenfilename(title="Select WebP file", filetypes=(("WebP files", "*.webp"), ("All files", "*.*")))
        if webp_file_path:
            convert_webp_to_png(webp_file_path)
    
    convert_button = tk.Button(root, text="Convert WebP to PNG", command=select_file_and_convert)
    convert_button.pack(pady=20)

    root.mainloop()
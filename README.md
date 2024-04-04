# WebP to PNG Converter

Download link: [WebP-to-PNG-Converter-win32.zip](https://github.com/vorlie/WebP_to_PNG_converter/releases/download/v1.0/WebP-to-PNG-Converter-win32.zip)
The file above works only on Windows 10+

## Editing the Registry File * optional

To add the "WebP to PNG converter" program to the context menu in Windows, follow these steps:

1. Open Notepad or any text editor.
2. Copy the following content:

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\WebP to PNG converter]
@="Convert WebP to PNG"
"Icon"=""PATH TO THE CONVERTER ICO\icon.ico""

[HKEY_CLASSES_ROOT\Directory\Background\shell\WebP to PNG converter\command]
@=""PATH TO THE CONVERTER EXE\converter.exe""
```

3. Replace `"PATH TO THE CONVERTER ICO"` with the path to the folder containing the `icon.ico` file.
4. Replace `"PATH TO THE CONVERTER EXE"` with the path to the folder containing the `converter.py` file.
5. Save the file with a `.reg` extension (e.g., `webp_to_png.reg`).
6. Double-click the `.reg` file to add the context menu entry to the Windows Registry.

## Using the Program

1. Double-click the `converter.exe` file to launch the "WebP to PNG converter" program.
    - If the context menu setup was done correctly, you should see the "WebP to PNG converter" program in the context menu. Opening the program from the context menu is faster than locating and opening the `converter.exe` file directly on your computer. Simply right-click and select the program from the context menu for quick access.
2. Click the button "Select WebP file" to select the WebP files you want to convert.
3. The converted PNG file will be saved in the same directory as the original WebP file.

Enjoy converting your WebP images to PNG with ease using the context menu integration!
